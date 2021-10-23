import random
num_1, num_2 = int(input('введите число от 0 до 20:  ')), int(input('введите число от 0 до 20:  '))
print('выбираются рандомные числа...')
num_ran_1, num_ran_2 = random.randint(1, 20), random.randint(1, 20)
count_1 = 0
count_2 = 0
spis_1 = []
for i in range(7):
    if (num_1 + num_2) > (num_ran_1 + num_ran_2):
        count_1 += 1
        spis_1.append(num_ran_1)
        spis_1.append(num_ran_2)
        num_1, num_2 = int(input('введите число от 0 до 20:  ')), int(input('введите число от 0 до 20:  '))
        print('выбираются рандомные числа...')
        num_ran_1, num_ran_2 = random.randint(1, 20), random.randint(1, 20)
    elif (num_1 + num_2) <= (num_ran_1 + num_ran_2):
        count_2 += 1
        spis_1.append(num_ran_1)
        spis_1.append(num_ran_2)
        num_1, num_2 = int(input('введите число от 0 до 20:  ')), int(input('введите число от 0 до 20:  '))
        print('выбираются рандомные числа...')
        num_ran_1, num_ran_2 = random.randint(1, 20), random.randint(1, 20)
if count_1 > count_2:
    print('пара введенных чисел больше пары рандомных на', (count_1 - count_2), 'раз')
else:
    print('пара введенных чисел меньше или равна паре рандомных. Список рандомных чисел в 4 итерации', spis_1[:8])




