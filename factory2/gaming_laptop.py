from abc import ABCMeta, abstractmethod


class ILaptop(metaclass=ABCMeta):
    """Gaming Laptop Interface"""

    @staticmethod
    @abstractmethod
    def get_price()->int:
        """The price of the Gaming Laptop"""

    @staticmethod
    @abstractmethod
    def get_specs()->dict:
        """The specifications of the Gaming Laptop"""


class LenovoLegion(ILaptop):
    """Concrete Product Creator for Lenovo"""

    def __init__(self):
        self._price : int = 75000
        self._cpu : str = "i9 13900HX" 
        self._gpu : str = "RTX 4090"
        self._ram : str = "64GB"

    def get_price(self):
        return self._price

    def get_specs(self):
        return {
                "CPU" : self._cpu,
                "GPU" : self._gpu,
                "RAM" : self._ram
                }

    def __str__(self):
        return "Lenovo Legion Pro 71"


class AsusROGZephyrus(ILaptop):
    """Concrete Product Creator for Asus"""

    def __init__(self):
        self._price : int = 78000
        self._cpu : str = "AMD Ryzen 9 6900HS" 
        self._gpu : str = "AMD Radeon RX 6800s"
        self._ram : str = "64GB"

    def get_price(self):
        return self._price

    def get_specs(self):
        return {
                "CPU" : self._cpu,
                "GPU" : self._gpu,
                "RAM" : self._ram
                }

    def __str__(self):
        return "Asus ROG Zephyrus G14"


class AcerPredatorHelios(ILaptop):
    """Concrete Product Creator for Acer"""

    def __init__(self):
        self._price : int = 72000
        self._cpu : str = "i9 13900HX" 
        self._gpu : str = "RTX 4080"
        self._ram : str = "32GB"

    def get_price(self):
        return self._price

    def get_specs(self):
        return {
                "CPU" : self._cpu,
                "GPU" : self._gpu,
                "RAM" : self._ram
                }
    def __str__(self):
        return "Acer Predator Helios 16"


class GamingLaptopFactory:
    """Gaming Laptop Creator/Factory"""

    @staticmethod
    def get_gaming_laptop(laptop : str):
        if laptop == "Lenovo":
            return LenovoLegion()
        if laptop == "Asus":
            return AsusROGZephyrus()
        if laptop == "Acer":
            return AcerPredatorHelios()
