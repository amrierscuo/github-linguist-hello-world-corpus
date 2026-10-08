from pathlib import Path
import json, shlex, subprocess, sys
build = Path(sys.argv[1]).resolve()
build.mkdir(parents=True, exist_ok=True)
def linux(path):
    p = Path(path).resolve().as_posix()
    return "/mnt/" + p[0].lower() + "/" + p[3:]
steps = []
def run(args, home=None):
    prefix = "env GNUPGHOME=" + shlex.quote(linux(home)) + " " if home else ""
    command = "cd " + shlex.quote(linux(build)) + " && " + prefix + " ".join(shlex.quote(str(a)) for a in args)
    p = subprocess.run(["wsl", "-d", "Ubuntu", "--", "sh", "-c", command], capture_output=True, text=True, encoding="utf8", errors="replace", timeout=60)
    step = {"command": " ".join(shlex.quote(str(a)) for a in args), "cwd": linux(build), "environment": {"GNUPGHOME": linux(home)} if home else {}, "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
    steps.append(step)
    assert p.returncode == 0, step
    return p.stdout
source = Path("greeting.txt").read_text(encoding="utf8").strip()
assert source == "Hello, World!"
uid = source + " <corpus@example.invalid>"
producer = build / "producer-keyring"
consumer = build / "consumer-keyring"
producer.mkdir(exist_ok=True)
consumer.mkdir(exist_ok=True)
run(["gpg", "--version"])
run(["chmod", "700", linux(producer), linux(consumer)])
run(["gpg", "--batch", "--pinentry-mode", "loopback", "--passphrase", "", "--quick-generate-key", uid, "ed25519", "sign", "0"], producer)
public = run(["gpg", "--batch", "--armor", "--export", "corpus@example.invalid"], producer)
assert "BEGIN PGP PUBLIC KEY BLOCK" in public
(build / "hello.asc").write_text(public, encoding="utf8", newline="\n")
run(["gpg", "--batch", "--import", "hello.asc"], consumer)
listed = run(["gpg", "--batch", "--with-colons", "--fingerprint", "--list-keys", "corpus@example.invalid"], consumer)
uids = [row.split(":")[9] for row in listed.splitlines() if row.startswith("uid:")]
assert uids == [uid], uids
assert any(row.startswith("pub:") and row.split(":")[3] == "22" for row in listed.splitlines())
print(json.dumps({"steps": steps, "uid": uids[0], "public_file": str(build / "hello.asc")}, ensure_ascii=False))
