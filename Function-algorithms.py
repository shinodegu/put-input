import re

def function():
    if number.isdigit():
        chislo = int(number)
        return 'Вы ввели целое положительное число', chislo
    elif re.fullmatch(r'-\d+', number):
        return "Вы ввели целое отрциательное число", number
    elif re.fullmatch(r'\d*[,.]\d+', number):
        return 'Вы ввели дробное положительное число', number
    elif re.fullmatch(r'-\d*[,.]\d+', number):
        return "Вы ввели дробное отрицательное число", number
    elif not number.isdigit():
        return 'Вы ввели некоректное число', number





while True:
    number = input("Введите число: ")
    if number.upper() in ("ВЫХОД", "E", "EXIT", "QUIT", "Q"):
        break
    print(*function())




























