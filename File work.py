a = input()
b = input()
c = input()
v = input()

file = open("aboba.txt", "w")
file.write(a), file.write('\n'), file.write(b), file.write('\n')
file.close()

file = open("aboba.txt", 'a')
file.write(c), file.write('\n'), file.write(v), file.write('\n')
file.close()
