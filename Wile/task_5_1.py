count_1 = 0
while True:
    count_1 += 1
    str_1 = input('введите слово:  ')
    if str_1 == 'стоп' or str_1 == 'хватит' or str_1 == 'достаточно':
        print('конец цикла')
        break
    print(f'{count_1} слов Вы ввели')

