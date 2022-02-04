class Stationery:

    def __init__(self, title: str) -> None:
        self.title = title

    def draw(self) -> None:
        if self.__class__.__name__ == 'Pencil':
            print('Запуск отрисовки')
            print(f'{self.__class__.__name__}:приступил к отрисовке объекта "{self.title}"')
        else:
            print(f'{self.__class__.__name__}:приступил к отрисовке объекта "{self.title}"')


# определите классы ниже согласно условий задания
class Pen(Stationery): ...
class Pencil(Stationery): ...
class Handle(Stationery): ...


if __name__ == '__main__':
    pen = Pen('Ручка')
    pencil = Pencil('Карандаш')
    handle = Handle('Маркер')
    pen.draw()  # Pen: приступил к отрисовке объекта "Ручка"
    handle.draw()  # Handle: приступил к отрисовке объекта "Маркер"
    pencil.draw()  # Пример вывода ниже в многострочном комментарии
    """
    Запуск отрисовки
    Pencil: приступил к отрисовке объекта "Карандаш"
    """