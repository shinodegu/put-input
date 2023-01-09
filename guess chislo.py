import random

popitok = 0

number = random.randint(1, 45)

print("Угадай число от 1 до 45. У тебя есть 3 попытки")

while popitok < 3:
    attempt = int(input())
    popitok += 1
    if attempt != number:
        print('Не угадал')
    elif attempt == number:
        print('Угадал')
        break

