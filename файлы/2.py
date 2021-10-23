file = open('byron.txt')
while True:
    line = file.readline()
    if line == 4:
        print(line)
    file.close()
