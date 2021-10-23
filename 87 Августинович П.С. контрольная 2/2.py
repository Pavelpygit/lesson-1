my_list = [1, 3, 4, 2, 5, 1, 20, 6, 2, 7, 5, 9, 4]
list_2 = []
count_1 = 0
a = 0
for i in my_list:
    a += 1
    if i in my_list[a:]:
        list_2.append(i)
        count_1 += 1
print(list_2)
print(count_1)





