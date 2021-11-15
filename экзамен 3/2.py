def palindrom(str_1):
    pal = str_1
    if pal == pal[::-1]:
        print(pal, '-- слово палиндром')
    else:
        print(pal, '-- слово не палиндром')
palindrom(input('введите слово:  '))


