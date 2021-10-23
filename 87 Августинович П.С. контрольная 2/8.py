file_1 = open('class.txt')
my_file = file_1.readlines()
for i in my_file:
    if i[2] > '3':
        print(i)
file_1.close()
# не понимаю как вытянуть число из строки текста...