list_1 = ['black', 'red', 'green', 'yelow']
list_2 = ['#00000', '#ff0000', '#80000', '#ffff0']
my_list = []
my_dict = {}
for i in list_1:
    my_dict['color_name'] = i
    for j in list_2:
        my_dict['color_code'] = j
        my_list.append(my_dict)
        my_dict = {}
print(my_list)