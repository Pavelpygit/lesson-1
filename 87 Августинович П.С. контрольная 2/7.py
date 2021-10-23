try:
    a = int(input())
    b = 100 / a
    print(b)
except ZeroDivisionError:
    print('на 0 делить нельзя')
finally:
    print('the end')

