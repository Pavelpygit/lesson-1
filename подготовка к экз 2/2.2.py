k_1 = [(1,2,5),(3,4),(5,6,4,8),(4,1,6,87,5)]
k_2 = []
a = 0
for i in k_1:
    for j in i:
        a = a + j
    k_2.append(a)
    a = 0
print(k_2)

