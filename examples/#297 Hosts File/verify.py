from pathlib import Path
from python_hosts import Hosts
hosts = Hosts(path=str(Path("hosts").resolve()))
entries = [entry for entry in hosts.entries if entry.entry_type == "ipv4"]
assert len(entries) == 1
assert entries[0].address == "192.0.2.1"
assert entries[0].names == ["hello-world.example.invalid"]
print("PASS: hello-world.example.invalid -> 192.0.2.1 (fixture only)")
