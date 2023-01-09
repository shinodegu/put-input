lst = (1, 3, 4, 5, 5, 6, 7, 7, 9, 9813, 'tgs', 4, 'rr', 7, 'r', 2482, 1, 3)


slovar = {}

for element in lst:
    if slovar.get(element, None):

        slovar[element] = 1 + slovar[element]

    else:
        slovar[element] = 1

print(slovar)