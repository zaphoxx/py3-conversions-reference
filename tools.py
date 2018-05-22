# reference for hex byte string conversions in python3
print("[+] references")
s = 'hack the world'
print("[+] {:30} : {}".format("string s".ljust(30),s))

# string to bytes
b = s.encode('utf-8')
print("[+] {:30} : {}".format("to bytes: s.encode('utf-8')",b))

# bytes to string
s2 = b.decode('utf-8')
print("[+] {:30} : {}".format("to string: b.decode('utf-8')",s2))

# bytes to hexstring
h = b.hex()
print("[+] {:30} : {}".format("to hex: b.hex()",h))

# from hex to bytes
b2 = bytes.fromhex(h)
print("[+] {:30} : {}".format("hex to bytes: bytes.fromhex(h)",b2))

# from string to bin
b3 = bin(int.from_bytes(s.encode('utf-8'),'little'))
print("[+] {:30} : \n\t{}".format("string to bin: \n\t[+] bin(int.from_bytes(s.encode('utf-8'),'little'))",b3))

# int to its char representative and backwards
x = 65
print("[x] x = {}".format(x))
print("[+] {:30} : {}".format("int to char: chr(x)",chr(x)))
print("[+] {:30} : {}".format("char to int: ord(x)",ord(chr(x))))

# number (base10 or base16 representation) as string to int
c = '1337'
print("[+] c = \'1337\'")
print("[+] {:30} : {}".format("number as string to int: int(c,10)",int(c,10)))
print("[+] {:30} : {}".format("hex as string to int: int(c,16)",int(c,16)))

# int to bytes
print("[+] {:30} : {}".format("byte(s) from int: int(c,16).to_bytes(2,'little')",int(c,16).to_bytes(2,'little')))
