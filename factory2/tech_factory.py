from gaming_laptop import GamingLaptopFactory
from gaming_monitor import GamingMonitorFactory

GAMING_LAPTOP_PRODUCTS = [
        "Lenovo",
        "Asus",
        "Acer"
        ]

MONITOR_PRODUCTS = [
        "Dell",
        "Asus",
        "Samsung",
        ]

class TechFactory:
    """Tech Factory"""

    
    @staticmethod
    def buy_product( product : str, product_type : str ):
        if product in GAMING_LAPTOP_PRODUCTS and product_type == "laptop":
            return GamingLaptopFactory.get_gaming_laptop(laptop=product)
        elif product in MONITOR_PRODUCTS and product_type == "monitor":
            return GamingMonitorFactory.get_gaming_monitor(monitor=product)
        return None
print("")
customer_1 = TechFactory.buy_product(product="Lenovo", product_type="laptop")
print(f"Customer 1 buy laptop: {customer_1}")
print(f"Customer 1: {customer_1.get_price()}")
print(f"Customer 1: {customer_1.get_specs()}")
customer_1_monitor = TechFactory.buy_product(product="Dell", product_type="monitor")
print(f"Customer 1 buy monitor: {customer_1_monitor}")
print(f"Customer 1: {customer_1_monitor.get_price()}")
print(f"Customer 1: {customer_1_monitor.get_size()}")
print(f"Customer 1: {customer_1_monitor.get_pixel_type()}")
print(f"Customer 1: {customer_1_monitor.get_max_refresh_rate()}")

print("")
customer_2 = TechFactory.buy_product(product="Asus", product_type="laptop")
print(f"Customer 2 buy laptop: {customer_2}")
print(f"Customer 2: {customer_2.get_price()}")
print(f"Customer 2: {customer_2.get_specs()}")
customer_2_monitor = TechFactory.buy_product(product="Asus", product_type="monitor")
print(f"Customer 2 buy monitor: {customer_2_monitor}")
print(f"Customer 2: {customer_2_monitor.get_price()}")
print(f"Customer 2: {customer_2_monitor.get_size()}")
print(f"Customer 2: {customer_2_monitor.get_pixel_type()}")
print(f"Customer 2: {customer_2_monitor.get_max_refresh_rate()}")
