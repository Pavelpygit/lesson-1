list_1 = ['abc', 'qwe', '123']
list_2 = ['abc', '123', 'qwe']
count_1 = 0
if len(list_1) == len(list_2):
    for i in list_1:
        if i in list_2:
            count_1 += 1
            if count_1 == len(list_2):
                print('yes')
        else:
            print('no')
else:
    print('no')