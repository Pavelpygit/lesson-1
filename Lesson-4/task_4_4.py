a = 1
for i in range(10):
    n = int(input())
    if n == 0:
        continue
    a = a * int(n)
    print('произведение введенных чисел =  ', a)
