my_list = ['afda', '1221', 'op', 'sdfgf', '1221', 'op']
for i in my_list:
    if i in my_list:
        del my_list[0]
print(my_list)
