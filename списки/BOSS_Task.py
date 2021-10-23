ved_3 = 0
ved_5 = 0
print('загадка "От Стива Джобса". Есть два ведра 3 и 5 литра, и неограниченое количество воды.'
      'Как отмерить ровно 4 литра.')
while ved_5 != 4:
      if ved_5 == 5:
            que_3 = input('Выливаем (-) или перельем (+)?  ')
            if que_3 == '-':
                  que_4 = input('из какого ведра (3) или (5)?  ')
                  if que_4 == '3':
                        ved_3 -= ved_3
                  elif que_4 == '5':
                        ved_5 -= ved_5
            elif que_3 == '+':
                  que_4 = input('из какого ведра (3) или (5)?  ')
                  if que_4 == '3':
                        ved_3 -= ved_3
                  elif que_4 == '5':
                        ved_5 = (ved_5 - (3 - ved_3))
                        ved_3 = 3
                  que_2 = input('Выливаем (-) или перельем в ведро 5 (+)?  ')
                  if que_2 == '-':
                        ved_3 -= ved_3
                        print(ved_5, ved_3)
                  elif que_2 == '+':
                        ved_5 += ved_3
                        ved_3 -= ved_3
                        if ved_5 >= 5:
                              ved_3 = (ved_3 - (5 - ved_5))
                              if ved_3 > 3:
                                    ved_3 = 3
                              ved_5 = 5
                        print(ved_5, ved_3)
      que_1 = input('В какое ведро наберем воды?  ')
      if que_1 == '3':
            ved_3 += 3
            print('В ведре 3 набрано 3 литра воды')
            que_2 = input('Выливаем (-) или перельем в ведро 5 (+)?  ')
            if que_2 == '-':
                  ved_3 -= ved_3
                  print(ved_5, ved_3)
            elif que_2 == '+':
                  ved_5 += ved_3
                  ved_3 -= ved_3
                  if ved_5 >= 5:
                        ved_3 = (ved_3 - (5 - ved_5))
                        if ved_3 > 3:
                              ved_3 = 3
                        ved_5 = 5
                  print(ved_5,ved_3)
      elif que_1 == '5':
            ved_5 += 5
            print('В ведре 5 набрано 5 литра воды')
            que_2 = input('Выливаем (-) или перельем в ведро 3 (+)?  ')
            if que_2 == '-':
                  ved_5 -= 5
                  print(ved_5, ved_3)
            elif que_2 == '+':
                  ved_3 += 3
                  ved_5 -= 5
                  print(ved_5,ved_3)






