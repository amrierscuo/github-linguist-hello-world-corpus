const fs = require('node:fs');
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const { JSDOM, VirtualConsole } = require('jsdom');
const html = fs.readFileSync(process.argv[2], 'utf8');
const errors = [];
const vc = new VirtualConsole();
vc.on('jsdomError', error => errors.push(error.message));
const dom = new JSDOM(html, { runScripts: 'dangerously', pretendToBeVisual: true, virtualConsole: vc });
const document = dom.window.document;
const walker = document.createTreeWalker(document.body, dom.window.NodeFilter.SHOW_TEXT);
const visibleText = [];
for (let node; (node = walker.nextNode()); ) {
  if (!node.parentElement?.closest('script, style') && node.textContent.trim()) visibleText.push(node.textContent);
}
const snapshot = { text: visibleText.join(''), text_nodes: visibleText, errors,
  elm_main_available: typeof dom.window.Elm?.Main?.init === 'function',
  generated_html_sha256: crypto.createHash('sha256').update(html).digest('hex'),
  node: process.version, jsdom: require('jsdom/package.json').version };
assert.equal(snapshot.elm_main_available, true);
assert.deepEqual(errors, []);
assert.equal(snapshot.text, 'Hello, World!');
assert.deepEqual(snapshot.text_nodes, ['Hello, World!']);
assert.equal(document.getElementById('elm'), null);
const disabled = new JSDOM(html);
assert.equal(disabled.window.Elm, undefined);
assert.equal(disabled.window.document.getElementById('elm').textContent, '');
disabled.window.close();
snapshot.execution_disabled_control = 'empty mount, Elm undefined';
console.log(JSON.stringify(snapshot, null, 2));
dom.window.close();
