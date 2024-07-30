
string = "ws2_32.dll"

for i in range(0, len(string), 4):
    part = string[i:(i+4)]
    print(hex(int.from_bytes(part.encode("ascii"), byteorder="little")))

