import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { pathToFileURL } from 'node:url';

const tools = path.resolve(process.argv[2]);
const source = path.resolve(process.argv[3] || 'src/pages/index.astro');
const { transform } = await import(pathToFileURL(path.join(tools, 'node_modules/@astrojs/compiler/dist/node/index.js')));
const result = await transform(await fs.readFile(source, 'utf8'), {
  filename: source.replaceAll('\\', '/'),
  internalURL: 'astro/compiler-runtime',
  resultScopedSlot: true,
});
assert.ok(result.code.includes('createComponent'));
assert.ok(!result.diagnostics.some(d => d.severity === 1));
console.log('PASS: official Astro compiler transformed the actual component');
if (process.argv.includes('--syntax-only')) process.exit(0);

// Generated module stays in the isolated tool directory, where its Astro imports resolve.
const output = path.join(tools, 'verified-hello-component.mjs');
await fs.writeFile(output, result.code);
const { default: Component } = await import(pathToFileURL(output));
const { experimental_AstroContainer: AstroContainer } = await import(
  pathToFileURL(path.join(tools, 'node_modules/astro/dist/container/index.js'))
);
const container = await AstroContainer.create();
const html = await container.renderToString(Component);
assert.ok(html.includes('<h1>Hello, World!</h1>'), html);
console.log(html);
console.log('PASS: official Astro runtime rendered the exact greeting heading');
