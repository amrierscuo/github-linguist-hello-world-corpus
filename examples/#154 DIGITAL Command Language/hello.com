$ greeting = "Hello, " + "World!"
$ WRITE SYS$OUTPUT greeting
$ EXIT 1
