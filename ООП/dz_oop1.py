import string
class AlfaBet:
    #метод с 2 динам. свойствами
    def __init__(self, leng, letters):
        self.leng = leng
        self.letters = letters
    #выводит в консоль буквы алфавита
    def Print(self):
        print(self.letters)

    # возвращает кол-во букв
    def LettersNum(self):
        count_1 = 0
        for i in self.letters:
            count_1 += 1
        return print('количество букв', count_1)

class EnAlfaBet(AlfaBet):
    str_1 = string.ascii_letters
    def __init__(self, str_1):
        super().__init__()
        self.str_1 = str_1
        # приватное статическое св-во
        self.__letters_num = len(str_1)

    # принимает букву и определяет есть ли она в алфавите
    def is_en_letters(self):
        self.let = input('введите букву "En"')
        if self.let in self.str_1:
            print(True)
        else:
            print(False)

    @staticmethod
    def Example():
        return AlfaBet.Print()

enalfabet = EnAlfaBet()
enalfabet.LettersNum()
enalfabet.is_en_letters()
enalfabet.Print()
# не понял как переопределить метод...
# что-то не работает( укажите ошибки .
