from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    _DVD_CAPACITY = 15
    _CUSTOMER_CAPACITY = 10

    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @classmethod
    def dvd_capacity(cls) -> int:
        return cls._DVD_CAPACITY

    @classmethod
    def customer_capacity(cls) -> int:
        return cls._CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if len(self.customers) < self._CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if len(self.dvds) < self._DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str or None:
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [customer for customer in self.customers if customer.id == customer_id][0]

        if not dvd or not customer:
            return None

        if dvd.is_rented:
            if dvd in customer.rented_dvds:
                return f"{customer.name} has already rented {dvd.name}"
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str or None:
        dvd = [dvd for dvd in self.dvds if dvd.id == dvd_id][0]
        customer = [customer for customer in self.customers if customer.id == customer_id][0]

        if not dvd or not customer:
            return None

        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"

        return f"{customer.name} does not have that DVD"

    def __repr__(self) -> str:
        current_customers_and_dvds = []
        for customer in self.customers:
            current_customers_and_dvds.append(str(customer))
        for dvd in self.dvds:
            current_customers_and_dvds.append(str(dvd))

        return "\n".join(current_customers_and_dvds)
