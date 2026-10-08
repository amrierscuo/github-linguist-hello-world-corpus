from pathlib import Path
import json, os, shutil, subprocess, sys
root=Path(__file__).resolve().parent
n=int(sys.argv[1]);repo=Path(sys.argv[2]).resolve();git=sys.argv[3] if len(sys.argv)>3 else 'git'
repo.mkdir(parents=True,exist_ok=False)
env=dict(os.environ,GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=str(repo/'empty-config'),GIT_AUTHOR_NAME='Corpus Example',GIT_AUTHOR_EMAIL='hello@example.invalid',GIT_COMMITTER_NAME='Corpus Example',GIT_COMMITTER_EMAIL='hello@example.invalid',GIT_AUTHOR_DATE='2026-10-08T00:00:00+0000',GIT_COMMITTER_DATE='2026-10-08T00:00:00+0000')
(repo/'empty-config').write_text('',encoding='utf-8')
steps=[]
def command(*args):
    result=subprocess.run([git,*args],cwd=repo,env=env,capture_output=True,text=True,encoding='utf-8',check=True)
    steps.append({'command':'git '+' '.join(args),'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
    return result.stdout
command('--version');command('init','--initial-branch=main');command('config','core.autocrlf','false')
if n==246:
    shutil.copyfile(root/'.gitattributes',repo/'.gitattributes');shutil.copyfile(root/'hello.txt',repo/'hello.txt')
    actual=command('check-attr','text','eol','corpus-greeting','--','hello.txt')
    assert actual=='hello.txt: text: set\nhello.txt: eol: lf\nhello.txt: corpus-greeting: hello-world\n',actual
    command('add','.gitattributes','hello.txt')
    actual=command('show',':hello.txt');assert actual=='Hello, World!\n',actual
elif n==247:
    shutil.copyfile(root/'hello.txt',repo/'hello.txt');command('add','hello.txt')
    command('commit','--no-gpg-sign','--cleanup=verbatim','-F',str(root/'.gitmessage'))
    subject=command('log','-1','--format=%s');assert subject=='Hello, World!\n',subject
    body=command('cat-file','commit','HEAD').split('\n\n',1)[1];assert body==(root/'.gitmessage').read_text(encoding='utf-8'),body
elif n==248:
    value=command('config','--file',str(root/'.gitconfig'),'--get','corpus.greeting');assert value=='Hello, World!\n',value
elif n==249:
    shutil.copyfile(root/'before/hello.txt',repo/'hello.txt');command('add','hello.txt');command('commit','--no-gpg-sign','-m','Initial greeting')
    original=command('rev-parse','HEAD').strip()
    shutil.copyfile(root/'after/hello.txt',repo/'hello.txt');command('add','hello.txt');command('commit','--no-gpg-sign','-m','Format greeting')
    formatting=command('rev-parse','HEAD').strip()
    listing='# Formatting-only revision from the reproducible local Git fixture.\n'+formatting+'\n'
    existing=root/'.git-blame-ignore-revs'
    if existing.exists():assert existing.read_text(encoding='utf-8')==listing,'Recorded revision differs from reproduced fixture'
    else:existing.write_text(listing,encoding='utf-8')
    shutil.copyfile(existing,repo/'.git-blame-ignore-revs')
    ordinary=command('blame','--porcelain','hello.txt');assert ordinary.split()[0]==formatting
    ignored=command('blame','--ignore-revs-file','.git-blame-ignore-revs','--porcelain','hello.txt');assert ignored.split()[0]==original,ignored
    assert '\tHello, World!' in ignored,ignored
else:raise ValueError(n)
print(json.dumps({'ordinal':n,'assertions':'PASS','steps':steps},ensure_ascii=False,indent=2))
