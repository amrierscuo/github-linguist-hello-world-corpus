from pathlib import Path
import m3u8
playlist = m3u8.loads(Path("hello.m3u8").read_text(encoding="utf-8"))
assert len(playlist.segments) == 1
segment = playlist.segments[0]
assert segment.title == "Hello, World!"
assert segment.uri == "https://example.invalid/greeting.ts"
assert segment.duration == 1 and playlist.is_endlist
print(segment.title)
