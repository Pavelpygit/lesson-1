# Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – кол-во букв.
# Сделать проверку со всеми этими случаями.

def f_1(val):
    if isinstance(val, tuple):
        len_tup = 0
        for i in val:
            len_tup += len(i)
            return len_tup
    if isinstance(val, list):
        count_str = 0
        count_int = 0
        for i in val:
            if isinstance(i, str):
                count_str += 1
            else:
                count_int += 1
        return count_int, count_str
    if isinstance(val, int):
        count = 0
        for i in str(val):
            if int(i) %2 != 0:
                count += 1
        return count
    if isinstance(val, str):
        count_1 = 0
        for i in val:
            count_1 +=1
        return count_1
print(f_1(('kjh')))
