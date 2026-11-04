const fs = require('node:fs');
const postcss = require('postcss');
const customProperties = require('postcss-custom-properties');
(async () => {
  const result = await postcss([customProperties({preserve: false})]).process(fs.readFileSync('hello.postcss', 'utf8'), {from: 'hello.postcss'});
  let greeting;
  result.root.walkDecls('content', decl => greeting = decl.value);
  if (greeting !== '"Hello, World!"') throw new Error('Unexpected transformation');
  process.stdout.write(result.css);
})().catch(error => {console.error(error); process.exitCode = 1;});
