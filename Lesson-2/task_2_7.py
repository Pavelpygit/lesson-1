user_input = input('Введите, пожалуйста, номер месяца:  ')
month = int(user_input)
print('Вы ввели', month)
if month == 1:
    print('Дней в месяце 31')
elif month == 2:
    print('Дней в месяце 28')
elif month == 3:
    print('Дней в месяце 31')
elif month == 4:
    print('Дней в месяце 30')
elif month == 5:
    print('Дней в месяце 31')
elif month == 6:
    print('Дней в месяце 30')
elif month == 7:
    print('Дней в месяце 31')
elif month == 8:
    print('Дней в месяце 31')
elif month == 9:
    print('Дней в месяце 30')
elif month == 10:
    print('Дней в месяце 31')
elif month == 11:
    print('Дней в месяце 30')
elif month == 12:
    print('Дней в месяце 31')
else:
    print('Номер не корректен.')
    #долго мучался сгрупировать. получилось только до 8-го месяца, так как дальше 30 и 31 меняются местами. сил нет.
    #сделал правильно, но не красиво.





