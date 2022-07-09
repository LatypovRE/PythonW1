#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#Пример:
#- 6 -> да
#- 7 -> да
#- 1 -> нет

from ast import arg

x = int(input('Введите день недели числом от 1 до 7: '))

def week(x):
    if x == 1:
        return 'Нет'
    elif x == 2:
        return 'Нет'
    elif x == 3:
        return'Нет'
    elif x == 4:
        return 'Нет'
    elif x == 5:
        return'Нет'
    elif x == 6:
        return 'Да'
    elif x == 7:
        return 'Да'
    else:
        return 'Введите корректное число'
arg = x
print(week(arg))