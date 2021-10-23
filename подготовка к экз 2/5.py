my_list =  ['afda', 'op', 'sdfgf', '1221']
count_1 = 0
for i in my_list:
    if len(i)>=2 and i[0] == i[-1]:
        count_1 += 1
print(count_1)


