from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Некоректный тип данных!")
        if capacity_volume <= 0:
            raise ValueError("Недопустимое значение!")
        self.capacity_volume = capacity_volume
        self.occupied_volume = occupied_volume  # TODO инициализировать объект "Стакан"


if __name__ == "__main__":
    glass_1 = Glass(500, 100)
    print(glass_1)
    glass_2 = Glass(200, 200)
    print(glass_2)  # TODO инициализировать два объекта типа Glass

    glass_3 = Glass(-500, 0)
    print(glass_3)  # TODO попробовать инициализировать не корректные объекты
