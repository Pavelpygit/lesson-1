spis_gl = ['а', 'о', 'у', 'е', 'я', 'э', 'ю', 'ы', 'и']
text_1 = input()
len_text = len(text_1)
glas = 0
list_1 = []
for i in text_1:
    if i in spis_gl:
        glas += 1
        list_1.append(i)
sogl = len_text - glas
if glas == sogl:
    print(list_1)
print('гласные', glas)
print('согласные', sogl)


