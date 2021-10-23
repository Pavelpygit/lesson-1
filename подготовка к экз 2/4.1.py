file = open('byron1.txt')
list_1 = []
list_1.append(file.readlines())
print(list_1[0])
file.close()
