from abc import ABCMeta

from builder_interface import BuilderInterface
from house import House


class Builder(BuilderInterface, metaclass=ABCMeta):

    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.parts.append("Walls")
        return self

    def build_windows(self):
        self.house.parts.append("Windows")
        return self

    def build_floor(self):
        self.house.parts.append("Floor")
        return self

    def build_roof(self):
        self.house.parts.append("Roof")
        return self

    def get_result(self):
        return self.house
