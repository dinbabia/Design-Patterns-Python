from abc import ABCMeta, abstractmethod


class IBurger(metaclass=ABCMeta):
    """Burger Product Interface"""
    
    @staticmethod
    @abstractmethod
    def get_ingredients(self) -> list:
        """The ingredients of the Burger"""

class CheeseBurger(IBurger):
    """Cheese Burger Concrete Creator"""
        
    def __init__(self):
        self._ingredients = ['bread', 'cheese', 'patty', 'ketchup', 'mayo']

    def get_ingredients(self) ->list:
       return self._ingredients

    def __str__(self):
        return "Cheese Burger!!!"


class RegularBurger(IBurger):
    """Regular Burger Concrete Creator"""

    def __init__(self):
        self._ingredients = ['bread', 'patty', 'ketchup', 'mayo']

    def get_ingredients(self) -> list:
        return self._ingredients

    def __str__(self):
        return "Regular Burger!!!"


class TLCBurger(IBurger):
    """TLC Burder Concrete Creator that did not fully implemented the Burger Interface."""
    pass

# Regular Implementation with interface but without factory
order_1 = CheeseBurger()
print(f"Order 1 Get Ingredients: {order_1.get_ingredients()}")
print(f"Order 1 Ingredients: {order_1._ingredients}")
# Private attributes are attributes of a class that can only be accessed within the class itself.
# They can still be accessed from outside the class by name mangling.
# However, this is discouraged as it goes against the principle of encapsulation

order_2 = RegularBurger().get_ingredients()
print(order_2)
print(type(order_2))

# If order_3 is uncommented, it will give lint error when using pylint and will not run the file
try:
    order_3 = TLCBurger()
except TypeError:
    print("Order 3 will error since TLCBurger did not properly implemented the Burger Interface. Lint also shows error when using Pylint.")

# Implement Factory/Creator

class BurgerFactory:
    """The Burger Factory/Creator Class"""

    @staticmethod
    def buy_burger(burger_type : str):
        """Static method (does not need to instantiate) to buy burger"""
        if burger_type == "Cheese Burger":
            return CheeseBurger()
        if burger_type == "Regular Burger":
            return RegularBurger()
        return None

# Client
customer_1 = BurgerFactory.buy_burger( burger_type = "Cheese Burger" )
print(f"Customer 1: {customer_1}")
customer_2 = BurgerFactory.buy_burger( burger_type = "Regular Burger" )
print(f"Customer 2: {customer_2}")
customer_3 = BurgerFactory.buy_burger( burger_type = "Cheese Burger" )
print(f"Customer 3: {customer_3}")
