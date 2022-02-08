from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate(self) -> float:
        pass


class Coat(Clothes):
    def __init__(self, size: float or int):
        self._size = size

    @property
    def calculate(self):
        return f'{self._size / 6.5 + 0.5 : .2f}'


class Costume(Clothes):
    def __init__(self, height: float or int):
        self._height = height

    @property
    def calculate(self):
        return f'{2 * self._height + 0.3 : .2f}'


if __name__ == '__main__':
    coat = Coat(45.0)
    costume = Costume(3)

    print(coat.calculate)  # 7.42
    print(costume.calculate)  # 6.3
