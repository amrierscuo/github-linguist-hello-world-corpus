const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
// First argument: a directory containing npm-installed node_modules.
const modules = path.resolve(process.argv[2] || '.tools/node_modules');
const { Filter, InvalidFilter, BlockingFilter, AllowingFilter, CommentFilter } =
  require(path.join(modules, 'adblockpluscore/lib/filterClasses.js'));
const { CombinedMatcher } = require(path.join(modules, 'adblockpluscore/lib/matcher.js'));
const { contentTypes } = require(path.join(modules, 'adblockpluscore/lib/contentTypes.js'));
const file = process.argv[3] || 'hello.txt';
const lines = fs.readFileSync(file, 'utf8').split(/\r?\n/);
assert.equal(lines.shift(), '[Adblock Plus 2.0]');
const matcher = new CombinedMatcher();
let active = 0;
for (const line of lines.filter(line => line.length > 0)) {
  const filter = Filter.fromText(line);
  assert.ok(!(filter instanceof InvalidFilter), `Invalid filter: ${line}`);
  if (filter instanceof CommentFilter) continue;
  assert.ok(filter instanceof BlockingFilter || filter instanceof AllowingFilter);
  matcher.add(filter);
  active++;
}
assert.equal(active, 2);
const cases = [
  ['https://example.org/ads/banner.png', contentTypes.IMAGE, 'blocking'],
  ['https://example.org/ads/hello-world.png', contentTypes.IMAGE, 'allowing'],
  ['https://example.org/ads/banner.png', contentTypes.SCRIPT, null],
  ['https://example.org/content/hello-world.png', contentTypes.IMAGE, null],
  ['https://notexample.org/ads/banner.png', contentTypes.IMAGE, null],
];
for (const [url, resourceType, expected] of cases) {
  const result = matcher.match(url, resourceType, 'example.org');
  const actual = result instanceof BlockingFilter ? 'blocking' :
    result instanceof AllowingFilter ? 'allowing' : null;
  assert.equal(actual, expected, url);
  console.log(JSON.stringify({url, resourceType, decision: actual}));
}
// Genuine parser negative control: unknown filter option is rejected.
assert.ok(Filter.fromText('||example.org^$not-a-real-option') instanceof InvalidFilter);
console.log('PASS: 2 active filters; 5 engine decisions; invalid-option rejected');
