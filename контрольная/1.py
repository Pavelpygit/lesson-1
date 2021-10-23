num_1 = input('введите семизначное число  ')
ch_1 = 0
nch_1 = 0
sum_1 = 0
for i in num_1:
    i = int(i)
    if i % 2 == 0:
        ch_1 += 1
    else:
        nch_1 += 1
if ch_1 > nch_1:
    for i in num_1:
        i = int(i)
        sum_1 += i
    print(f'количество четных цифр больше. Сумма всех цифр = {sum_1}')
else:
    print(f' количество нечетных цифр больше. Произведение 1, 3 и 6 цифры = {int(num_1[0]) * int(num_1[2]) * int(num_1[5])}')




