import random
num_1 = int(input('введите количество рандомных чисел:  '))
num_2 = int(input('введите искомую цифру:  '))
spis_1 = []
spis_2 = 0
for i in range(num_1):
    spis_1.append(random.randint(0, num_1))
print(spis_1)
for i in spis_1:
 if num_2 == i:
    spis_2 += 1
print(f'цифра {num_2} встречается {spis_2} раз')
