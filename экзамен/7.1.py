byn_1 = float(input('введите рубли  '))
val_1 = input('введите валюту')
if val_1 == 'usd':
    print (f'usd = {byn_1 / 2.5}')
elif val_1 == 'eur':
    print(f'eur= {byn_1 / 3}')
elif val_1 == 'rub':
    print(f'rub= {byn_1 * 30.3}')
else:
    print('другой валюты нет')

