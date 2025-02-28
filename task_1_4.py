﻿ЗАДАНИЕ:
1)Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления
на ноль.
2)Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция должна 
принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.
3)Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.
4)Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить возведение числа x в степень y. Задание необходимо
реализовать в виде функции my_func(x, y). При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
##Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора **,
предусматривающая использование цикла.
5)Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после 
этого завершить программу.
6)Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. Например,
print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских
букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

РЕШЕНИЕ:
1)
def func(chislo_1, chislo_2):
    try:
        return chislo_1 / chislo_2
    except ZeroDivisionError:
        print("На ноль делить нельзя")


print(func(int(input("Делимое: ")), int(input("Делитель: "))))
__________________________________________________________________________________________________________________________________________________________________________
2)
def func(name, lastname, birth, city, mail, phone):
    return print(
        f"Имя: {name}, фамилия: {lastname}, год рождения: {birth},  город: {city}, почта: {mail}, номер телефона: {phone}")


func(
    name=input("Имя: "),
    lastname=input("Фамилия: "),
    birth=input("Год Рождения: "),
    city=input("Город: "),
    mail=input("Почта: "),
    phone=input("Номер телефона: "),
)
__________________________________________________________________________________________________________________________________________________________________________
3)
def func(chislo1, chislo2, chislo3):
    func_sort = sorted([chislo1, chislo2, chislo3])
    return func_sort[1] + func_sort[2]


spisok = [float(i) for i in input("Введите 3 числа через пробел: ").split()]
print(f"{func(spisok[0], spisok[1], spisok[2])}")
__________________________________________________________________________________________________________________________________________________________________________
4)
def func_1(x, y):
    return x ** y


def func_2(x, y):
    a = 1
    result = 1 / x
    while a < abs(y):
        result = result * (1 / x)
        a += 1
    return result


print("Результат по 1-му способу = ", func_1(int(input("Введите X: ")), int(input("Введите Y: "))))
print("Результат по 2-му способу = ", func_2(int(input("Введите X: ")), int(input("Введите Y: "))))
__________________________________________________________________________________________________________________________________________________________________________
5)
def f_convert_str(str_var):
    try:
        var_f = float(str_var)
    except ValueError:
        var_f = None
    return var_f


def f_processing_entering_string(str_var):
    result = 0
    stop_flag = False

    list_var = str_var.split()
    for var in list_var:
        convert_var = f_convert_str(var)
        if convert_var == None:
            stop_flag = True
            break
        result += convert_var

    return result, stop_flag


summ_itogo = 0

print("Вводите числа, разделенные пробелмаи, для выхода из программы введите любую букву")

stop_flag = False
while not stop_flag:
    str_var = input(":")
    current_sum, stop_flag = f_processing_entering_string(str_var)

    summ_itogo += current_sum

    print(f"Текущий результат суммирования = {summ_itogo}")
__________________________________________________________________________________________________________________________________________________________________________
6)
def int_func (*args):
    word = input("Введите слово/слова из латинских букв в нижнем регистре: ")
    print(word.title())
    return
int_func()
