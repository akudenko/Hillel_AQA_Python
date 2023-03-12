# Выбрать паттерн проектирования и реализовать его на конкретном примере
# (паттерн из GoF, который рассматривали или не рассматривали, но не Singleton, не Iterator, не Decorator).

from builder import Builder


class Main:

    @staticmethod
    def construct():
        return Builder()\
            .build_windows()\
            .build_floor()\
            .build_roof()\
            .build_walls()\
            .get_result()


house = Main.construct()
print(house.parts)
