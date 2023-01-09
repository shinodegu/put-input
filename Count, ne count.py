chislo = int(input('Введите число: '))



a = ((lambda chislo: ('нечетное') if chislo%2 != 0 else ('четное')))



print(a(chislo))

