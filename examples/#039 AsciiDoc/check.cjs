const fs = require('node:fs');
const assert = require('node:assert/strict');
const asciidoctor = require('@asciidoctor/core');
(async () => {
const logger = asciidoctor.MemoryLogger.create();
asciidoctor.LoggerManager.setLogger(logger);
const document = await asciidoctor.loadFile('hello.adoc', { safe: 'safe', standalone: true });
assert.equal(document.getDocumentTitle(), 'Greeting');
const blocks = document.getBlocks();
assert.equal(blocks.length, 1);
assert.equal(blocks[0].getContext(), 'paragraph');
assert.equal(blocks[0].getSource(), 'Hello, World!');
const html = await document.convert();
assert.ok(html.includes('<p>Hello, World!</p>'));
assert.deepEqual(logger.getMessages(), []);
console.log(`Asciidoctor.js ${asciidoctor.getVersion()}: title, paragraph and rendered HTML assertions passed; 0 diagnostics.`);
})().catch((error) => { console.error(error); process.exitCode = 1; });
