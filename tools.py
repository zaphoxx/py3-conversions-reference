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