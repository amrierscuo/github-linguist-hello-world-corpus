from pathlib import Path
from crontab import CronTab
import subprocess,json
cron=CronTab(tab=Path("crontab").read_text())
jobs=list(cron)
assert len(jobs)==1 and jobs[0].is_valid()
assert str(jobs[0].slices)=="0 9 * * *"
r=subprocess.run(["wsl","-e","sh","-c",jobs[0].command],capture_output=True,text=True)
assert r.returncode==0 and r.stdout=="Hello, World!\n"
print(json.dumps({"command":"sh -c <parsed-crontab-command>","exit_code":r.returncode,"stdout":r.stdout,"stderr":r.stderr}))
