"""Use the original ZenStack generator, Prisma SQL engine and SQLite default."""
import argparse
import os
from pathlib import Path
import sqlite3
import subprocess
import tempfile
import sys

sys.stdout.reconfigure(encoding='utf-8')

parser = argparse.ArgumentParser()
parser.add_argument('zenstack_tools', nargs='?', default='.tools')
parser.add_argument('prisma_tools', nargs='?', default='.tools-prisma')
parser.add_argument('--node', default='node')
args = parser.parse_args()
zenstack = Path(args.zenstack_tools).resolve()
prisma = Path(args.prisma_tools).resolve() / 'node_modules/prisma/build/index.js'
example = Path(__file__).resolve().parent
environment = {**os.environ, 'CHECKPOINT_DISABLE': '1', 'DO_NOT_TRACK': '1'}
with tempfile.TemporaryDirectory(prefix='corpus-zmodel-') as scratch:
    scratch = Path(scratch)
    def run(*command):
        result = subprocess.run([args.node, *map(str, command)], cwd=scratch,
            env=environment, capture_output=True, text=True, encoding='utf-8', check=True)
        print(result.stdout, end='')
        if result.stderr:
            print(result.stderr, end='')
        return result.stdout
    run(example / 'generate.cjs', zenstack, example / 'hello.zmodel', scratch / 'generated.prisma')
    run(prisma, 'validate', '--schema', 'generated.prisma')
    sql = run(prisma, 'migrate', 'diff', '--from-empty', '--to-schema-datamodel',
              'generated.prisma', '--script')
    assert sql.strip(), 'Prisma must generate a nonempty native SQL migration'
    database = sqlite3.connect(':memory:')
    database.executescript(sql)
    database.execute('INSERT INTO "Greeting" DEFAULT VALUES')
    row = database.execute('SELECT "id", "message" FROM "Greeting"').fetchone()
    assert row == (1, 'Hello, World!'), row
    print(row[1])
    print(f'PASS: generated Zmodel SQL default applied by SQLite {sqlite3.sqlite_version}')
