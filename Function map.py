values = [1, 2, '3', 'forth', 'end', 99, True, None]


for el in values:
    print(type(el), el)

values_2 = list(map(lambda x: str(x) if type(x) == int else (x), values))

print('#'*50)
for el in values_2:
    print(type(el), el)





