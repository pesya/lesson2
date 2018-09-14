#написать функцию, которая принимает на вход две строки
#Проверить, является ли то что переданно функции строками. Если нет - вернуть 0
#Если строки одинаковые, верунть 1
#Если строки разные и первая длиннее, вернуть 2
#Если строки разные и вторая строка 'learn', возвращает 3
#Вызвать функцию несколько раз, передавая ей разные праметры и выводя на экран результаты


def compare_strings(s1, s2):
    if s1.isalpha() == False or s2.isalpha() == False:
        return 0
    elif len(s1) == len(s2):
        return 1
    elif len(s1) > len(s2):
        return 2
    elif len(s1) != len(s2) and s2 == 'learn':
        return 3


a, b = input('Give me two words: ').split()
print(compare_strings(a, b))