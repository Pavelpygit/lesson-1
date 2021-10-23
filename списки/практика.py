list_1 = [i for i in range (10)]
for i in range (10):
    i += 1
    for j in list_1[1:]:
        print(i * j)
# как вывести каждый в отдельный список не понимаю