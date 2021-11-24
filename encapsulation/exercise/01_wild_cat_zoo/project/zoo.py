from project.lion import Lion
from project.tiger import Tiger
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.caretaker import Caretaker
from project.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []
        self.type_of_animal = {"Lion": [], "Tiger": [], "Cheetah": [], "Total": 0}
        self.type_of_worker = {"Keeper": [], "Caretaker": [], "Vet": [], "Total": 0}

    def add_animal(self, animal, price):
        if len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        self.type_of_animal[type(animal).__name__].append(animal)
        self.type_of_animal["Total"] += 1
        return f"{animal.name} the {type(animal).__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) >= self.__workers_capacity:
            return "Not enough space for worker"

        self.workers.append(worker)
        self.type_of_worker[type(worker).__name__].append(worker)
        self.type_of_worker["Total"] += 1
        return f"{worker.name} the {type(worker).__name__} hired successfully"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.type_of_worker[type(worker).__name__].remove(worker)
                self.type_of_worker["Total"] -= 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        all_salaries = 0
        for worker in self.workers:
            all_salaries += worker.salary

        if self.__budget < all_salaries:
            return "You have no budget to pay your workers. They are unhappy"

        self.__budget -= all_salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        budget_required = 0
        for animal in self.animals:
            budget_required += animal.money_for_care

        if self.__budget < budget_required:
            return "You have no budget to tend the animals. They are unhappy."

        self.__budget -= budget_required
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animals_count = len(self.animals)
        print_data = [f"You have {animals_count} animals", f"----- {len(self.type_of_animal['Lion'])} Lions:"]
        for animal in self.animals:
            if type(animal).__name__ == "Lion":
                print_data.append(animal.__repr__())
        print_data.append(f"----- {len(self.type_of_animal['Tiger'])} Tigers:")
        for animal in self.animals:
            if type(animal).__name__ == "Tiger":
                print_data.append(animal.__repr__())
        print_data.append(f"----- {len(self.type_of_animal['Cheetah'])} Cheetahs:")
        for animal in self.animals:
            if type(animal).__name__ == "Cheetah":
                print_data.append(animal.__repr__())
        return "\n".join(print_data)

    def workers_status(self):
        workers_count = len(self.workers)
        print_data = [f"You have {workers_count} workers", f"----- {len(self.type_of_worker['Keeper'])} Keepers:"]
        for worker in self.workers:
            if type(worker).__name__ == "Keeper":
                print_data.append(worker.__repr__())
        print_data.append(f"----- {len(self.type_of_worker['Caretaker'])} Caretakers:")
        for worker in self.workers:
            if type(worker).__name__ == "Caretaker":
                print_data.append(worker.__repr__())
        print_data.append(f"----- {len(self.type_of_worker['Vet'])} Vets:")
        for worker in self.workers:
            if type(worker).__name__ == "Vet":
                print_data.append(worker.__repr__())
        return "\n".join(print_data)


# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4), Lion("Neo", "Male", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140, 170]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Firing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())
