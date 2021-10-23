with open('registration_good.log.txt', 'w', encoding='utf-8') as f_good:
    with open('registration_bad.log.txt', 'w', encoding='utf-8') as f_bad:
        with open ('registrations.txt', encoding='utf-8') as file:
            for i in file:
                if len(i.split()) == 3:
                    if i.split()[0].isalpha():
                        if '@' and '.' in i.split()[1]:
                            if i.split()[2].isdigit():
                                if 10 < int(i.split()[2]) < 99:
                                    f_good.write(i)
                                else:
                                    f_bad.write('поле возраст НЕ является числом от 10 до 99 -  ')
                                    f_bad.write(i)
                            else:
                                f_bad.write('поле имени содержит НЕ только буквы -  ')
                                f_bad.write(i)
                        else:
                            f_bad.write('поле емейл НЕ содержит @ и .(точку) -  ')
                            f_bad.write(i)
                    else:
                        f_bad.write('поле имени содержит НЕ только буквы -  ')
                        f_bad.write(i)
                else:
                    f_bad.write('НЕ присутсвуют все три поля  -  ')
                    f_bad.write(i)




