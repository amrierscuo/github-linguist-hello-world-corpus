import pathlib,sys
p=pathlib.Path(sys.argv[1]);p.parent.mkdir(parents=True,exist_ok=True);p.write_text("Hello, World!\n",encoding="utf-8")
