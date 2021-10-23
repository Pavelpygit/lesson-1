spis_1 = [1,20,5,4,6,12,3]
spis_2 = [2,12,6,5,7,9,30]
a = set(spis_1)
b = set(spis_2)
c = a.intersection(b)
count_1 = 0
for i in c:
    count_1 +=1
print(f'{c} \n'
      f'одновременно содержится в 2-х списках {count_1} числа')