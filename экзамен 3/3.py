class Tomato:
    states = {
        'low': 0,
        'mid': 50,
        'high': 100
    }
    def __init__(self, index, state = states['low']):
        self._index = index
        self._state = state

    def grow(self):
        if self._state == 0:
            self._state = Tomato.states['mid']
        elif self._state == 50:
            self._state = Tomato.states['high']

    def is_ripe(self):
        if self._state == 100:
            print('томат созрел')
        else:
            print('томат не созрел')

class TomatoBush:
    def __init__(self, q_tomat):
        self.q_tomat = q_tomat
        self.tomatoes = []
        for i in range(q_tomat):
            tomato = Tomato(1)
            self.tomatoes.append(tomato)

    def grow_all(self):
        for i in self.tomatoes:
            Tomato.grow(i)

    def all_are_ripe(self):
        for i in self.tomatoes:
            Tomato.is_ripe(i)
            if Tomato.is_ripe(i) == 100:
                return True

    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, _plant):
        self.name = name
        self._plant = Tomato(1)

    def work(self):
        TomatoBush.grow_all()

    def harvest(self):
        harvest = []
        if Tomato.states['high'] is self._plant:
            harvest.append(self._plant)
        else:
            print('ёще не все созрели')

    @staticmethod
    def knowledge_base():
        print(Gardener(name='Mike', _plant= Tomato(1)))
        print(TomatoBush(10))

# Тесты
if __name__ == '__main__':
    Gardener.knowledge_base()
    tb = TomatoBush(10)
    g = Gardener(name='Mike', _plant= Tomato(1))
    g.work()
    g.harvest()
    g.work()
    g.harvest()



