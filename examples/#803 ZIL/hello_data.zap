	; Data to accompany hello.zap

	FLAGS2=0
	EXTAB=0
	TCHARS=0

	CEXIT=4
	CEXITFLAG=1
	CEXITSTR=1
	DEXIT=5
	DEXITOBJ=1
	DEXITSTR=1
	FALSE-VALUE=0
	FATAL-VALUE=2
	FEXIT=3
	FEXITFCN=0
	NEXIT=2
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
	UEXIT=1

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
	.BYTE 7
	.WORD 4
	.VOCBEG 7,4
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
