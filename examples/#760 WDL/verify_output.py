"""Check the actual results of `miniwdl run hello.wdl > result.json`."""
import argparse
import json
from pathlib import Path

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("result_json", type=Path)
args = parser.parse_args()
result = json.loads(args.result_json.read_text(encoding="utf-8"))
assert result["outputs"] == {"greeting.message": "Hello, World!"}, result
run_dir = Path(result["dir"])
saved_outputs = json.loads((run_dir / "outputs.json").read_text(encoding="utf-8"))
assert saved_outputs == result["outputs"], saved_outputs
task_stdout = (run_dir / "call-hello" / "stdout.txt").read_text(encoding="utf-8")
task_stderr = (run_dir / "call-hello" / "stderr.txt").read_text(encoding="utf-8")
assert task_stdout == "Hello, World!\n", repr(task_stdout)
assert task_stderr == "", task_stderr
print(json.dumps({
    "outputs": saved_outputs,
    "task_stdout": task_stdout,
    "task_stderr": task_stderr,
    "assertion": "PASS: original miniwdl executes hello task and evaluates workflow output",
}, indent=2))
