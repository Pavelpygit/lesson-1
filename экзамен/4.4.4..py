i_1 = [3, 6, 12, 5, 2, 4, 17]
a = min(i_1)
for i in i_1:
   if i > a:
       a += 1
       if i == a:
        print(i)
        break