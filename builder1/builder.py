class Laptop():
    """Laptop product"""
    
    def __init__(self, brand_name : str ):
        """Laptop Attributes.
        You can add parameters for more flexibility like brand_name."""
        self.brand_name = brand_name
        self.price = None
        self.cpu = None
        self.gpu = None

    def __str__(self):
        return f"Brand: {self.brand_name}\nPrice: {self.price}\nCPU: {self.cpu}\nGPU: {self.gpu}"


from abc import ABCMeta, abstractmethod

class ILaptop(metaclass=ABCMeta):
    """Laptop Builder Interface"""

    @staticmethod
    @abstractmethod
    def set_price( price : int):
        """Set the price of the Laptop"""

    @staticmethod
    @abstractmethod
    def set_cpu( cpu : str ):
        """Set the cpu of the laptop"""

    @staticmethod
    @abstractmethod
    def set_gpu( gpu : str ):
        """Set gpu of the laptop"""


class LaptopBuilder(ILaptop):
    """Laptop Builder"""

    def __init__(self, brand_name : str):
        self.low_acer = Laptop(brand_name=brand_name)

    def set_price(self, price : int):
        self.low_acer.price = price
        return self

    def set_cpu(self, cpu : str):
        self.low_acer.cpu = cpu
        return self

    def set_gpu(self, gpu : str):
        self.low_acer.gpu = gpu
        return self

    def build(self):
        return self.low_acer


# Test if working
product_1 = LaptopBuilder(brand_name="Acer") \
        .set_price(50000) \
        .set_cpu("i9") \
        .set_gpu("RTX 3090") \
        .build()
print(product_1)
print("\n")


# No parameter to Director
class LowEndAcerDirector:

    @staticmethod
    def build():
        return LaptopBuilder(brand_name="Acer") \
        .set_price(50000) \
        .set_cpu("i7") \
        .set_gpu("RTX 3090") \
        .build()

# Client giving no parameter
low_end_acer = LowEndAcerDirector.build() 
print("Low End Acer")
print(low_end_acer)
print("\n")

# With paramter to Director
class MidEndAcerDirector:

    @staticmethod
    def build(price : int):
        return LaptopBuilder(brand_name="Acer") \
        .set_price(price) \
        .set_cpu("i9") \
        .set_gpu("RTX 3090") \
        .build()

# Client giving parameter
mid_end_acer = MidEndAcerDirector.build(price = 60000) 
print("Middle End Acer")
print(mid_end_acer)
print("\n")

