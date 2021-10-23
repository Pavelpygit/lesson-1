my_list = [1, 2, 3, 4, 5, 1, 2, 3, 9]
list_2 = []
for i in my_list:
    if i in my_list[i:]:
        continue
    list_2.append(i)
print(list_2)






