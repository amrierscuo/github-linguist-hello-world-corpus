import pysrt
items=pysrt.open('hello.srt',encoding='utf-8',error_handling=pysrt.ERROR_RAISE)
assert len(items)==1 and items[0].index==1
assert items[0].start.ordinal==0 and items[0].end.ordinal==2000
assert items[0].text=='Hello, World!'
print(items[0].text);print('PASS: existing SubRip parser validates timing/index and subtitle text')
