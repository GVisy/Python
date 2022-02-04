import time


class TrafficLight:
    __color: list = ['красный', 'жёлтый', 'зелёный']
    __timer: list = [4, 2, 3]

    def running(self):
        indx = 0
        while indx < len(self.__color):
            print(f'{self.__color[indx]} {self.__timer[indx]} сек')
            time.sleep(self.__timer[indx])
            indx += 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()