from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def find(self, product_name: str):
        for obj in self.products:
            if obj.name == product_name:
                return obj

    def remove(self, product_name: str):
        for obj in self.products:
            if obj.name == product_name:
                self.products.remove(obj)

    def __repr__(self):
        products_list = []
        for obj in self.products:
            products_list.append(f"{obj.name}: {obj.quantity}")

        return "\n".join(products_list)


# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)
