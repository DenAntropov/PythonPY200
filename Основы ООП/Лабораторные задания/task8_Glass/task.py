# TODO Добавить методы add_water и remove_water
from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float], add_water: Union[int, float], remove_water: Union[int, float]):
        self.capacity_volume = None
        self.init_capacity_volume(capacity_volume)

        self.occupied_volume = None
        self.init_occupied_volume(occupied_volume)

        self.add_water = None
        self.init_add_water(add_water)

        self.remove_water = None
        self.init_remove_water(remove_water)

    def init_capacity_volume(self, capacity_volume: [int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if not capacity_volume > 0:
            raise ValueError
        self.capacity_volume = capacity_volume

    def init_occupied_volume(self, occupied_volume):
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError
        if occupied_volume < 0:
            raise ValueError
        self.occupied_volume = occupied_volume

    def add_water(self, add_water):
        if not isinstance(add_water, (int, float)):
            raise TypeError
        if add_water > self.capacity_volume - self.occupied_volume:
            raise ValueError
        self.add_water = add_water

    def remove_water(self, remove_water):
        if not isinstance(remove_water, (int, float)):
            raise TypeError
        if remove_water > self.occupied_volume:
            raise ValueError
        self.remove_water = remove_water


if __name__ == "__main__":
    glass = Glass(200, 100, 50, 25)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume, glass.add_water, glass.remove_water)
