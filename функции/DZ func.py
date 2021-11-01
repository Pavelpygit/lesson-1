# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
a = int(input())
b = int(input())
def f_1():
    return a + b
def f_2():
    return a - b
def f_3():
    return a * b
def f_4():
    if b == 0:
        print("error")
    else:
        return a / b
while True:
    operation = input()
    if operation == "0":
        break
    else:
        if operation == "+":
            print(f_1())
        if operation == "-":
            print(f_2())
        if operation == "*":
            print(f_3())
        if operation == "/":
            print(f_4())
    a = int(input())
    b = int(input())
