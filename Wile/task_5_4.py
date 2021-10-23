money_1 = int(input('Средств на карте:  '))
chek_1 = int(input('расходы:  '))
sum_1 = 0
num_1 = 0
while money_1 > chek_1:
    sum_1 +=chek_1
    money_1 -= chek_1
    num_1 += 1
    chek_1 = int(input('расходы:  '))
if money_1 < sum_1:
    print(f'сделали {num_1} покупок. Остаток на карте {money_1}')


