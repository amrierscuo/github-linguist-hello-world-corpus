# Block II AGC example: explicit ASCII codes, one 15-bit word per character.
# ASCII is a convention of this example, not a native AGC text service.
# Starting at octal 4000, load H (octal 00110) into A and hold.
                SETLOC  4000
START           CA      GREET
HOLD            TC      HOLD
GREET           OCT     00110    # 'H'
                OCT     00145    # 'e'
                OCT     00154    # 'l'
                OCT     00154    # 'l'
                OCT     00157    # 'o'
                OCT     00054    # ','
                OCT     00040    # ' '
                OCT     00127    # 'W'
                OCT     00157    # 'o'
                OCT     00162    # 'r'
                OCT     00154    # 'l'
                OCT     00144    # 'd'
                OCT     00041    # '!'
