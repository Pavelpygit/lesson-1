spis_gl = ['e', 'y', 'u', 'i', 'o', 'a']
str_1 = input('введите строку EN с разным регистром:  ')
len_str_1 = len(str_1)
glas = 0
spis_1 = [str_1[0]]
count_l = 0
count_u = 0
for i in str_1.lower():
    if i in spis_gl:
        glas += 1
for i in str_1[1:]:
    if i.islower():
        if spis_1 [-1].islower() == i.islower():
            count_l += 1
        spis_1.append(i)
    elif i.isupper():
        if spis_1[-1].isupper() == i.isupper():
            count_u += 1
        spis_1.append(i)
sogl = len_str_1 - glas
print(f'{count_l} пары нижнего регистра, {count_u} пары верхнего регистра')
print('гласных', glas)
print('согласных', sogl)
print(f'длина строки {len_str_1} символов')
# 3 символа подряд одного регистра считает как 2 пары ну и т.д. надеюсь так правильно