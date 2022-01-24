import zlib
var1 = "hello world!hello world!hello world!hello world!"
var2 = bytes(var1, "utf-8")
var3 = zlib.compress(var2)
print(var3)
print(zlib.decompress(var3))
