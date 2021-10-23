str_1 = 'hbkHYVK'
dic_1 = {}
n_1 = 0
n_2 = 0
for i in str_1:
    if i.isupper():
        n_1 += 1
        dic_1['upper'] = n_1
    else:
        n_2 += 1
        dic_1['lower'] = n_2
print(dic_1)

