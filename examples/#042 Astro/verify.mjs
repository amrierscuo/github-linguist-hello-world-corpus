import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

const tools = path.resolve(process.argv[2] || '.tools');
const source = path.resolve(process.argv[3] || 'src/pages/index.astro');
const scratch = await fs.mkdtemp(path.join(tools, 'corpus-astro-'));
await fs.mkdir(path.join(scratch, 'src/pages'), { recursive: true });
await fs.copyFile(source, path.join(scratch, 'src/pages/index.astro'));
await fs.writeFile(path.join(scratch, 'package.json'), JSON.stringify({
  name: 'corpus-astro-verification', private: true, type: 'module',
  dependencies: { astro: '5.14.1' },
}));
await fs.symlink(path.join(tools, 'node_modules'), path.join(scratch, 'node_modules'),
  process.platform === 'win32' ? 'junction' : 'dir');
const build = spawnSync(process.execPath, [path.join(tools, 'node_modules/astro/astro.js'),
  'build', '--root', scratch], { encoding: 'utf8', cwd: scratch,
  env: { ...process.env, ASTRO_TELEMETRY_DISABLED: '1' } });
process.stdout.write(build.stdout || '');
process.stderr.write(build.stderr || '');
assert.equal(build.status, 0, 'Official Astro build failed');
if (process.argv.includes('--syntax-only')) process.exit(0);
const html = await fs.readFile(path.join(scratch, 'dist/index.html'), 'utf8');
assert.ok(html.includes('<h1>Hello, World!</h1>'), html);
console.log(html);
console.log('PASS: official Astro static renderer evaluated the frontmatter and greeting');
