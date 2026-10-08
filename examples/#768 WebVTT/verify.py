import webvtt
captions=list(webvtt.read('hello.vtt'));assert len(captions)==1
c=captions[0];assert c.start=='00:00:00.000' and c.end=='00:00:02.000'
assert c.text=='Hello, World!'
print(c.text);print('PASS: existing WebVTT decoder verifies cue timing and text')
