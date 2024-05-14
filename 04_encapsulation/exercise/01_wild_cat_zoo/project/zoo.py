from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:
    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int) -> None:
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: int) -> str:
        if self.__budget < price:
            return "Not enough budget"
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker) -> str:
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str) -> str:
        try:
            worker = [w for w in self.workers if w.name == worker_name][0]
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        except IndexError:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self) -> str:
        total_workers_salaries = sum([w.salary for w in self.workers])

        if total_workers_salaries <= self.__budget:
            self.__budget -= total_workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self) -> str:
        total_animals_expenses = sum([a.money_for_care for a in self.animals])

        if total_animals_expenses <= self.__budget:
            self.__budget -= total_animals_expenses
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount: int) -> None:
        self.__budget += amount

    def animals_status(self) -> str:
        result = f"You have {len(self.animals)} animals\n"

        lions = [a for a in self.animals if a.__class__.__name__ == "Lion"]
        tigers = [a for a in self.animals if a.__class__.__name__ == "Tiger"]
        cheetahs = [a for a in self.animals if a.__class__.__name__ == "Cheetah"]

        result += f"----- {len(lions)} Lions:\n"
        for lion in lions:
            result += f"{lion}\n"
        result += f"----- {len(tigers)} Tigers:\n"
        for tiger in tigers:
            result += f"{tiger}\n"
        result += f"----- {len(cheetahs)} Cheetahs:\n"
        for cheetah in cheetahs:
            result += f"{cheetah}\n"

        return result[:-1]

    def workers_status(self) -> str:
        result = [f"You have {len(self.workers)} workers"]

        keepers = [w for w in self.workers if w.__class__.__name__ == "Keeper"]
        caretakers = [w for w in self.workers if w.__class__.__name__ == "Caretaker"]
        vets = [w for w in self.workers if w.__class__.__name__ == "Vet"]

        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(f"{keeper}")
        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(f"{caretaker}")
        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(f"{vet}")

        return "\n".join(result)
