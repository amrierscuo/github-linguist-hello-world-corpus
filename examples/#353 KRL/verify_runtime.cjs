/* Run the real Picolab engine locally without a web server or persistent store. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const { createRequire } = require('node:module');

async function main() {
  const dependencies = path.resolve(process.argv[2] || '.tools');
  const load = createRequire(path.join(dependencies, 'package.json'));
  const { PicoEngineCore, RulesetRegistryLoaderMem } = load('pico-engine-core');
  const { MemoryLevel } = load('memory-level');
  const db = new MemoryLevel({ keyEncoding: load('charwise'), valueEncoding: 'json' });
  const source = fs.readFileSync(path.join(__dirname, 'hello.krl'), 'utf8');
  const rulesetUrl = 'https://corpus.invalid/hello.krl';
  const engineErrors = [];
  const log = {
    debug() {}, info() {}, warn() {},
    child() { return log; },
    error(message, detail) { engineErrors.push({ message, detail }); },
  };
  const engine = new PicoEngineCore({
    db, log, getPicoLogs: async () => [], autoCreateRootPico: false,
    rsRegLoader: RulesetRegistryLoaderMem(async (url) => {
      assert.equal(url, rulesetUrl);
      return source;
    }),
  });
  try {
    await engine.start();
    const loaded = await engine.rsRegistry.load(rulesetUrl);
    assert.equal(loaded.rid, 'io.corpus.greeting');
    const pico = await engine.picoFramework.createRootPico();
    await pico.install(loaded.ruleset, { url: rulesetUrl });
    const channel = await pico.newChannel({
      tags: ['corpus-test'],
      eventPolicy: { allow: [{ domain: 'corpus', name: '*' }], deny: [] },
      queryPolicy: { allow: [], deny: [] },
    });
    const event = (name) => ({
      eci: channel.id, domain: 'corpus', name, data: { attrs: {} }, time: Date.now(),
    });
    const unrelated = await engine.eventWait(event('unrelated'));
    assert.deepEqual(unrelated.directives, []);
    const result = await engine.eventWait(event('hello'));
    assert.equal(result.directives.length, 1);
    const directive = result.directives[0];
    assert.equal(directive.name, 'greeting');
    assert.equal(directive.options.message, 'Hello, World!');
    assert.deepEqual(engineErrors, []);
    console.log(JSON.stringify({
      engine: 'pico-engine-core', engine_version: engine.version,
      compiler_version: loaded.compiler.version,
      ruleset: loaded.rid, installed_rulesets: Object.keys(pico.rulesets),
      negative_event: { domain: 'corpus', name: 'unrelated', directives: unrelated.directives },
      event: { domain: 'corpus', name: 'hello' },
      directives: result.directives,
      assertion: 'PASS: installed original KRL ruleset emits greeting with message Hello, World!',
    }, null, 2));
    await pico.uninstall(loaded.rid);
  } finally {
    await db.close();
    await load('node-schedule').gracefulShutdown();
  }
}

main().catch((error) => {
  console.error(error.stack || String(error));
  process.exitCode = 1;
});
