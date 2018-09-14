#Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError если приведение типов не сработало


def get_sum():
    try:
        x,y = map(int, input('I need 2 integer numbers please: ').split())
    except:
        print('Please give me an integer')
        return
    print(x+y)


get_sum()
