#Попросить пользователя ввести возраст при помощи input и положить результат в переменную
#Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: учиться в детском саду, школе, ВУЗе или работать
#Вызвать функцию, передав ей возраст пользователя и положить результат работы функции в преременную
#Вывести содержимое переменной на экран


user_age = int(input('Give me your age: '))


def what_user_do(age):
    if age < 8:
        return  'You are at kindergarten!'
    elif 8 <= age < 18:
        return  'You are at school!'
    elif 18 <= age < 25:
        return 'You are at university!'
    else:
        return 'You are working ;('


print(what_user_do(user_age))