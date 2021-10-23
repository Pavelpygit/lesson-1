a, b = 1, 5
c, d = 10, 25
num_1 = int(input())
count_1 = 0
while True:
    if num_1 >= 25:
        num_1 -= 25
        count_1 +=1
        print(d, '+', end=' ')
    elif num_1 >= 10:
        num_1 -= 10
        count_1 += 1
        print(c, '+', end=' ')
    elif num_1 >= 5:
        num_1 -= 5
        count_1 += 1
        print(b, '+', end=' ')
    elif num_1 < 5 and num_1 > 0:
        num_1 -= 1
        count_1 += 1
        print(a, '+', end=' ')
    elif num_1 == 0:
        break
print('     ', count_1, 'монет заплатили')




