def cr_card(num):
    num_card = num
    len_num_card = len(str(num_card))
    num_2 = ''
    for i in str(num_card):
        if len(num_2) <= len_num_card - 5:
            num_2 += '*'
        else:
            num_2 += i
    print(num_2)
cr_card(input('number card:  '))









