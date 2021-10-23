i_1 = [17, 2, 4, 12]
i_2 = [10, 5, 4, 7]
i_3 = []
for i in i_1:
    for j in i_2:
        i_3.append(i * j)
print(i_3[::5])