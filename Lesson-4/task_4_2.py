num_1 = int(input('m  '))
num_2 = int(input('n  '))
if num_1 > num_2:
    for i in range(num_1, num_2 + 1, -1):
        print(i)
else:
    for i in range(num_1, num_2 + 1):
        print(i)