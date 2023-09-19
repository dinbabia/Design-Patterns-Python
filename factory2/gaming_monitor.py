from abc import ABCMeta, abstractmethod


class IMonitor(metaclass=ABCMeta):
    """Gaming Monitor Interface"""

    @staticmethod
    @abstractmethod
    def get_price()->int:
        """Price of the monitor."""

    @staticmethod
    @abstractmethod
    def get_size()->int:
        """Size of the monitor."""

    @staticmethod
    @abstractmethod
    def get_pixel_type()->str:
        """Size of the monitor."""

    @staticmethod
    @abstractmethod
    def get_max_refresh_rate()->str:
        """Size of the monitor."""

class DellAlienware(IMonitor):
    """Concrete Creator for Dell Alienware"""

    def __init__(self):
        self._price : int = 32000
        self._size : int = 34
        self._pixel_type : str = "QD-OLED"
        self._max_refresh_rate : str = "175 Hz"

    def get_price(self):
        return self._price

    def get_size(self):
        return self._size

    def get_pixel_type(self):
        return self._pixel_type

    def get_max_refresh_rate(self):
        return self._max_refresh_rate

    def __str__(self):
        return """Dell Alienware AW3423DW"""


class AsusSwiftOled(IMonitor):
    """Concrete Creator for Asus Swift OLED"""

    def __init__(self):
        self._price : int = 29000
        self._size : int = 27
        self._pixel_type : str = "OLED"
        self._max_refresh_rate : str = "240 Hz"

    def get_price(self):
        return self._price

    def get_size(self):
        return self._size

    def get_pixel_type(self):
        return self._pixel_type

    def get_max_refresh_rate(self):
        return self._max_refresh_rate

    def __str__(self):
        return """Asus ROG Swift OLED PG27AQDM"""

class SamsungOdyssey(IMonitor):
    """Concrete Creator for Samsung Odysey"""

    def __init__(self):
        self._price : int = 31000
        self._size : int = 32
        self._pixel_type : str = "VA"
        self._max_refresh_rate : str = "240 Hz"

    def get_price(self):
        return self._price

    def get_size(self):
        return self._size

    def get_pixel_type(self):
        return self._pixel_type

    def get_max_refresh_rate(self):
        return self._max_refresh_rate

    def __str__(self):
        return """Samsung Odyssey Neo G8 S32BG85"""

class GamingMonitorFactory:

    @staticmethod
    def get_gaming_monitor( monitor :str ):
        if monitor == "Dell":
            return DellAlienware()
        if monitor == "Asus":
            return AsusSwiftOled()
        if monitor == "Samsung":
            return SamsungOdyssey()
