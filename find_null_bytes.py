import keystone


CODE = (
"""

"""
)

# Initialize engine in X86-32bit mode
ks = keystone.Ks(keystone.KS_ARCH_X86, keystone.KS_MODE_32)

encoding, count = ks.asm(CODE)
print("Encoded %d instructions..." % count)

shellcode = ""
for dec in encoding:
    if dec == 0:
        print(hex(dec))

