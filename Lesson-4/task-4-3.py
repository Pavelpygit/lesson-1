n = int(input('Введите натуральное число:  '))
for i in range (1, n + 1):
    if i == 1:
        print(i, '+')
    elif i == 2 or i == 3 or i == 5 or i == 7:
        print(i, '++')
    elif i == 4 or i == 9:
        print(i, '+++')
    else:
        print(i, '++++')
