a = Analysis(['greet.py'], pathex=[], binaries=[], datas=[], hiddenimports=[])
p = PYZ(a.pure)
e = EXE(p, a.scripts, a.binaries, a.datas, name='corpus-greeting', console=True)
