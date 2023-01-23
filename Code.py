a = b'r\xc3\xa9sum\xc3\xa9'
print(a)

b = a.decode()
print(b)


z = b.encode('Latin1')
print(z)

x = z.decode('Latin1')
print(x)
