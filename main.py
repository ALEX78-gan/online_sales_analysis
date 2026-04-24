from product import Product
from product_manager import ProductManager
from cart import Cart
import random

pm = ProductManager()

pm.add_product(Product("Laptop", 1000, 5))
pm.add_product(Product("Telefon", 500, 10))
pm.add_product(Product("Casti", 100, 20))
pm.add_product(Product("Mouse", 50, 30))

cart = Cart()

products = pm.products
selected_products = random.sample(products, 3)

for product in selected_products:
    cart.add_to_cart(product)

cart.display_cart()
print("Total de plata:", cart.total_price())

