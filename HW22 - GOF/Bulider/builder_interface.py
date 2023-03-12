from abc import ABCMeta, abstractmethod


class BuilderInterface(metaclass=ABCMeta):
    # Builder Interface

    @staticmethod
    @abstractmethod
    def build_walls():
        pass

    @staticmethod
    @abstractmethod
    def build_floor():
        pass

    @staticmethod
    @abstractmethod
    def build_windows():
        pass

    @staticmethod
    @abstractmethod
    def build_roof():
        pass

    @staticmethod
    @abstractmethod
    def get_result():
        pass
