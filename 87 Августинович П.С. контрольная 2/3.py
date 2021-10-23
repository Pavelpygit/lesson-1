c_1 = (35, 78, 21, 37, 2, 98, 6, 100, 231)
c_2 = (45, 21, 124, 76, 5, 23, 91, 234)
count_1 = 0
count_2 = 0
for i in c_1:
    count_1 += i
for j in c_2:
    count_2 += j
if count_1 > count_2:
    print(f'сумма с_1={count_1} больше чем сумма c_2={count_2}')
elif count_1 < count_2:
    print(f'сумма с_1={count_1} меньше чем сумма c_2={count_2}')
else:
    print(f'суммы равны {count_1} = {count_2}')
print('минимальное значение списка с_1=', min(c_1), 'и его индекс', c_1.index(min(c_1)))
print('максимальное значение списка с_1=', max(c_1), 'и его индекс',c_1.index(max(c_1)))
print('минимальное значение списка с_2=', min(c_2), 'и его индекс',c_2.index(min(c_2)))
print('максимальное значение списка с_2=', max(c_2), 'и его индекс',c_2.index(max(c_2)))


