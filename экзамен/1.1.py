sec_1 = int(input())
hou_1 = 0
min_1 = 0
sec_2 = 0
while sec_1 > sec_2:
    if sec_1 > 3600:
        hou_1 +=1
        sec_1 -= 3600
    elif sec_1 > 60:
        min_1 += 1
        sec_1 -= 60
    elif sec_1 < 60:
        sec_2 += sec_1
        break
print(f'{hou_1} часов {min_1} минут {sec_2} секнд')

