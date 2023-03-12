from abc import ABCMeta


class BuilderInterface(metaclass=ABCMeta):
    # Builder Interface

    @staticmethod
    def build_walls():
        pass

    @staticmethod
    def build_floor():
        pass

    @staticmethod
    def build_windows():
        pass

    @staticmethod
    def build_roof():
        pass

    @staticmethod
    def get_result():
        pass
