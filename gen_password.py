# ГЕНЕРАТОР ПАРОЛЕЙ
import string
import random
import time

count_pass = 0
len_pass = 0
parameters = ''


def start():
    print(
        """Для взаимодействия с программой используй команды:
    1 - означает да
    2 - означает нет""")
    time.sleep(1)
    print("Программа которая генерирует пароли. \nГотовы начать?")

    a = int(input())
    if a == 1:
        pass_count()
    else:
        print('Счастливо!')
        time.sleep(1)


def pass_count():
    global count_pass
    try:
        count_pass = int(input("Укажите сколько вам нужно паролей \n(максимум 100)"))
        if 1 <= count_pass <= 100:
            pass_len()
        else:
            print("Вы ввели некорректное число")
            time.sleep(1.2)

    except ValueError:
        print("Введите целое число не больше 100")
        time.sleep(1.2)


def pass_len():
    global len_pass
    try:
        len_pass = int(input("Укажите длину пароля \n(от 8 до 30) "))
        if 8 <= len_pass <= 30:
            other_details()
        else:
            print("Вы указали некорректную длину")
            time.sleep(1.2)

    except ValueError:
        print("Введите целое число не меньше 8 и не больше 30")
        time.sleep(1.2)


def other_details():
    global parameters
    no = 0
    try:
        print("Использовать цифры в пароле?")
        answer = int(input())
        if answer == 1:
            parameters += string.digits
        else:
            no += 1

        print("Использовать верхний регистр букв в пароле?")
        answer = int(input())
        if answer == 1:
            parameters += string.ascii_uppercase
        else:
            no += 1

        print("Использовать нижний регистр букв в пароле?")
        answer = int(input())
        if answer == 1:
            parameters += string.ascii_lowercase
        else:
            no += 1

        print("Использовать пунктуацию в пароле?")
        answer = int(input())
        if answer == 1:
            parameters += string.punctuation
        else:
            no += 1

        if no <= 2:
            create_pass()

        else:
            print("Вы выбрали слишком мало параметров для пароля! \nИз чего мне пароль делать...")
    except ValueError:
        print("Ошибочка... Что-то не то вы ввели")
        time.sleep(1.2)


def create_pass():
    global parameters, len_pass, count_pass
    passwords = ''
    for i in range(count_pass):
        password = ''
        for y in range(len_pass):
            password += random.choice(parameters)
        passwords += password + '\n'

    print("Ваш результат: ", passwords)
    time.sleep(5)
    replay()


def replay():
    print('Вам нужно еще сгенерировать пароли?')
    a = int(input())
    if a == 1:
        pass_count()
    else:
        print("Счастливо!")
        time.sleep(1)


start()
