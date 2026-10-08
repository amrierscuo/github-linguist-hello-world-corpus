	; Data to accompany hello.xzap

	FLAGS=0
	FLAGS2=0
	EXTAB=0
	TCHARS=0
	CHRSET=0

	CEXIT=5
	CEXITFLAG=4
	CEXITSTR=1
	DEXIT=6
	DEXITOBJ=1
	DEXITSTR=2
	FALSE-VALUE=0
	FATAL-VALUE=2
	FEXIT=4
	FEXITFCN=0
	NEXIT=3
	NEXITSTR=0
	P1?ADJECTIVE=2
	P1?DIRECTION=3
	P1?OBJECT=0
	P1?VERB=1
	PS?ADJECTIVE=32
	PS?BUZZ-WORD=4
	PS?DIRECTION=16
	PS?OBJECT=128
	PS?PREPOSITION=8
	PS?VERB=64
	REXIT=0
	SERIAL=0
	TRUE-VALUE=1
	UEXIT=2
	RELEASEID=0

GLOBAL:: .TABLE
	.GVAR PREPOSITIONS=PRTBL
	.GVAR ACTIONS=ATBL
	.GVAR PREACTIONS=PATBL
	.GVAR VERBS=VTBL
	.ENDT

OBJECT:: .TABLE
	; Unused property #1
	.WORD 0
	; Unused property #2
	.WORD 0
	; Unused property #3
	.WORD 0
	; Unused property #4
	.WORD 0
	; Unused property #5
	.WORD 0
	; Unused property #6
	.WORD 0
	; Unused property #7
	.WORD 0
	; Unused property #8
	.WORD 0
	; Unused property #9
	.WORD 0
	; Unused property #10
	.WORD 0
	; Unused property #11
	.WORD 0
	; Unused property #12
	.WORD 0
	; Unused property #13
	.WORD 0
	; Unused property #14
	.WORD 0
	; Unused property #15
	.WORD 0
	; Unused property #16
	.WORD 0
	; Unused property #17
	.WORD 0
	; Unused property #18
	.WORD 0
	; Unused property #19
	.WORD 0
	; Unused property #20
	.WORD 0
	; Unused property #21
	.WORD 0
	; Unused property #22
	.WORD 0
	; Unused property #23
	.WORD 0
	; Unused property #24
	.WORD 0
	; Unused property #25
	.WORD 0
	; Unused property #26
	.WORD 0
	; Unused property #27
	.WORD 0
	; Unused property #28
	.WORD 0
	; Unused property #29
	.WORD 0
	; Unused property #30
	.WORD 0
	; Unused property #31
	.WORD 0
	; Unused property #32
	.WORD 0
	; Unused property #33
	.WORD 0
	; Unused property #34
	.WORD 0
	; Unused property #35
	.WORD 0
	; Unused property #36
	.WORD 0
	; Unused property #37
	.WORD 0
	; Unused property #38
	.WORD 0
	; Unused property #39
	.WORD 0
	; Unused property #40
	.WORD 0
	; Unused property #41
	.WORD 0
	; Unused property #42
	.WORD 0
	; Unused property #43
	.WORD 0
	; Unused property #44
	.WORD 0
	; Unused property #45
	.WORD 0
	; Unused property #46
	.WORD 0
	; Unused property #47
	.WORD 0
	; Unused property #48
	.WORD 0
	; Unused property #49
	.WORD 0
	; Unused property #50
	.WORD 0
	; Unused property #51
	.WORD 0
	; Unused property #52
	.WORD 0
	; Unused property #53
	.WORD 0
	; Unused property #54
	.WORD 0
	; Unused property #55
	.WORD 0
	; Unused property #56
	.WORD 0
	; Unused property #57
	.WORD 0
	; Unused property #58
	.WORD 0
	; Unused property #59
	.WORD 0
	; Unused property #60
	.WORD 0
	; Unused property #61
	.WORD 0
	; Unused property #62
	.WORD 0
	; Unused property #63
	.WORD 0
	.ENDT

IMPURE::

PRTBL:: .TABLE 2
	.WORD 0
	.ENDT

VTBL:: .TABLE 510
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0,0,0,0,0,0
	.WORD 0,0,0,0,0
	.ENDT

ATBL:: .TABLE 0

	.ENDT

PATBL:: .TABLE 0

	.ENDT

VOCAB:: .TABLE
	.BYTE 3
	.BYTE 44
	.BYTE 46
	.BYTE 34
	.BYTE 9
	.WORD 4
	.VOCBEG 9,6
W?$QUOTE:: .ZWORD """"
	.BYTE 0,0,0
W?$APOSTROPHE:: .ZWORD "'"
	.BYTE 0,0,0
W?$COMMA:: .ZWORD ","
	.BYTE 0,0,0
W?$PERIOD:: .ZWORD "."
	.BYTE 0,0,0
	.VOCEND
	.ENDT

ENDLOD::
	.ENDI
