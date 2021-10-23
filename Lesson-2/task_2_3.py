word_1 = input('введите слово')
if len(word_1) > 5:
    print(word_1)
elif len(word_1) < 5:
    print('Need more')
elif len(word_1) == 5:
    print('It is five')