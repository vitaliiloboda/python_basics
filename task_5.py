class Stationery:
    title = 'канцелярская принадлежность'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'ручка'

    def draw(self):
        print(f'Отрисовка ({self.title})')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print(f'Отрисовка ({self.title})')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print(f'Отрисовка ({self.title})')


a = Stationery()
a.draw()

b = Pen()
b.draw()

c = Pencil()
c.draw()

d = Handle()
d.draw()
