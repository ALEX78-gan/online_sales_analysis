from product import Product
from product_manager import ProductManager

pm = ProductManager()

p1 = Product("Tv", 2000, 5)

p3 = Product("Mouse", 200, 20)

pm.add_product(p1)

pm.add_product(p3)

