from product import Product
from product_manager import ProductManager

pm = ProductManager()

p1 = Product("Laptop", 1000, 5)
p2 = Product("Telefon", 500, 10)
p3 = Product("Casti", 100, 20)

pm.add_product(p1)
pm.add_product(p2)
pm.add_product(p3)

pm.display_products()
print("Valoare totala:", pm.total_value())