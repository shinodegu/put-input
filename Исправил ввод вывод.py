
bank = open('python.txt', 'w')

latter = input('Введите предложение через пробел:  ')

first = latter.split()

z = first[0]
x = first[1]



print(first[0], first[1], sep = ' >>> ', file=bank)
print(f'!{first[0][::-1].upper()}' , f'{first[1][::-1].capitalize()}?', sep = ' >>> ', file=bank)
print('!%s'  % (first[0][::-1].upper()), '%s?' % (first[1][::-1].capitalize()), sep = ' >>> ', file=bank)
print('!{}'.format(first[0][::-1].upper()),'{}?'.format(first[1][::-1].capitalize()), sep = ' >>> ', file=bank)




