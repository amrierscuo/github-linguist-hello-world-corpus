from pathlib import Path
import json, os, shutil, subprocess, sys
source=Path(__file__).resolve().parent
repo=Path(sys.argv[1]).resolve()
assert not repo.exists(), 'Require a new temporary repository'
repo.mkdir(parents=True)
empty=repo/'empty.gitconfig';empty.write_text('',encoding='utf-8')
env=dict(os.environ,GIT_CONFIG_NOSYSTEM='1',GIT_CONFIG_GLOBAL=str(empty),GIT_TERMINAL_PROMPT='0')
git=sys.argv[2] if len(sys.argv)>2 else 'git'
steps=[]
def run(args):
 r=subprocess.run([git]+args,cwd=repo,env=env,capture_output=True,text=True,encoding='utf-8')
 steps.append(dict(command='git '+' '.join(args),exit_code=r.returncode,stdout=r.stdout,stderr=r.stderr))
 return r
assert run(['--version']).returncode==0
assert run(['init','--quiet']).returncode==0
shutil.copyfile(source/'.gitignore',repo/'.gitignore')
shutil.copyfile(source/'hello.txt',repo/'hello.generated.txt')
(repo/'build').mkdir();(repo/'build/disposable.txt').write_text('temporary fixture',encoding='utf-8')
(repo/'other.generated.txt').write_text('temporary fixture',encoding='utf-8')
r=run(['check-ignore','--no-index','--verbose','build/disposable.txt','other.generated.txt','hello.generated.txt'])
assert r.returncode==0
assert '.gitignore:1:build/' in r.stdout and '.gitignore:2:*.generated.txt' in r.stdout and '.gitignore:3:!hello.generated.txt' in r.stdout
assert run(['check-ignore','hello.generated.txt']).returncode==1
assert (repo/'hello.generated.txt').read_text(encoding='utf-8')=='Hello, World!\n'
print(json.dumps(dict(assertions='PASS',steps=steps),ensure_ascii=False))
