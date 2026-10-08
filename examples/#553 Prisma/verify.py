"""Generate SQL with Prisma, then exercise its default in real SQLite."""
import argparse
import os
from pathlib import Path
import shutil
import sqlite3
import subprocess
import tempfile
import sys

sys.stdout.reconfigure(encoding='utf-8')

parser = argparse.ArgumentParser()
parser.add_argument('tools', nargs='?', default='.tools')
parser.add_argument('--node', default='node')
args = parser.parse_args()
cli = Path(args.tools).resolve() / 'node_modules/prisma/build/index.js'
source = Path(__file__).resolve().parent / 'hello.prisma'
environment = {**os.environ, 'CHECKPOINT_DISABLE': '1', 'PRISMA_HIDE_UPDATE_MESSAGE': '1'}
with tempfile.TemporaryDirectory(prefix='corpus-prisma-') as scratch:
    scratch = Path(scratch)
    shutil.copyfile(source, scratch / source.name)
    (scratch / 'prisma.config.ts').write_text(
        "export default { schema: 'hello.prisma', datasource: { url: 'file:./hello.db' } };\n",
        encoding='utf-8')
    def run(*command):
        result = subprocess.run([args.node, str(cli), *command], cwd=scratch,
            env=environment, capture_output=True, text=True, encoding='utf-8', check=True)
        print(result.stdout, end='')
        if result.stderr:
            print(result.stderr, end='')
        return result.stdout
    run('validate', '--schema', 'hello.prisma')
    sql = run('migrate', 'diff', '--from-empty', '--to-schema', 'hello.prisma', '--script')
    assert sql.strip(), 'Prisma must generate a nonempty native SQL migration'
    database = sqlite3.connect(':memory:')
    database.executescript(sql)
    database.execute('INSERT INTO "Greeting" ("id") VALUES (?)', (1,))
    row = database.execute('SELECT "id", "text" FROM "Greeting"').fetchone()
    assert row == (1, 'Hello, World!'), row
    print(row[1])
    print(f'PASS: Prisma SQL default applied by SQLite {sqlite3.sqlite_version}')
