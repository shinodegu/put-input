
keep = open('python.txt',  'w')

color = input('Enter a color: ')
place = input('Enter a place: ')
print(color, place,end='>>>',file=keep)
road1 = print(f'!{color[::-1].upper()} {place[::-1].capitalize()}?',end='>>>', file=keep)
road2 = print('!%s %s?' % (color[::-1].upper(), place[::-1].capitalize()),end='>>>', file=keep)
road3 = print('!{} {}?'.format(color[::-1].upper(), place[::-1].capitalize()),file=keep)



