dic_1 = {'a': 10, 'b': 20, 'c': 100}
dic_2 = {'a': 30, 'c': 40, 'd': 45}
dic_3 = {}
for i in dic_1:
    if i in dic_2:
        dic_3[i] = dic_1[i] + dic_2[i]
dic_2.update(dic_1)
dic_2.update(dic_3)
print(dic_2)