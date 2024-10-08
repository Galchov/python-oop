from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int) -> None:
        self.budget = budget

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        expenses, sponsors = self.team_financial_data
        revenue = 0

        for sponsor in sponsors.values():
            for position, money in sponsor.items():
                if race_pos <= position:
                    revenue += money
                    break

        revenue -= expenses
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

    @property
    @abstractmethod
    def team_financial_data(self) -> tuple:
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value
