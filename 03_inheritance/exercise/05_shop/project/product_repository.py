from project.product import Product

from project.drink import Drink
from project.food import Food


class ProductRepository:

    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        for product_obj in self.products:
            if product_obj.name == product_name:
                return product_obj

    def remove(self, product_name: str):
        for product_obj in self.products:
            if product_obj.name == product_name:
                self.products.remove(product_obj)

    def __repr__(self):
        print_info = []
        for product_obj in self.products:
            print_info.append(f"{product_obj.name}: {product_obj.quantity}")
        return "\n".join(print_info)


# Test code:
food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)
