str_1 = 'an apple a day keeps the doctor away'
dict_1 = {}
for i in str_1:
    if i == ' ':
        continue
    dict_1[i] = str_1.count(i)
print(dict_1)
