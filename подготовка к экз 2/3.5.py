dic_1 = {
    'ok': 12,
    'cb': 10,
    'kd': 12
}
list_1 = []
for i in dic_1:
    list_1.append(dic_1[i])
for j in list_1:
    if j != 12:
        print(False)
    else:
        print(True)

