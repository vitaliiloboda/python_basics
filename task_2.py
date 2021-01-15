from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def tissue_consumption(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size > 60:
            self.__size = 60
        elif size < 40:
            self.__size = 40
        else:
            self.__size = size

    @property
    def tissue_consumption(self):
        return self.size / 6.5 + 0.5


class Costume(Clothes):

    def __init__(self, growth):
        self.growth = growth

    @property
    def tissue_consumption(self):
        return 2 * self.growth + 0.3


coat = Coat(65)
print(f'Coat tissue consumption: {round(coat.tissue_consumption, 2)}')

costume = Costume(1.8)
print(f'Costume tissue consumption: {round(costume.tissue_consumption, 2)}')

total_tissue_consumption = round(sum([coat.tissue_consumption, costume.tissue_consumption]), 2)
print(f'Total tissue consumption: {total_tissue_consumption}')
