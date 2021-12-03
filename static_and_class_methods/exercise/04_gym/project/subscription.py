class Subscription:
    __id = 1

    def __init__(self, date: str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = Subscription.__assign_next_id()

    @classmethod
    def __assign_next_id(cls):
        next_id = Subscription.__id
        Subscription.__id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Subscription.__id

    def __repr__(self):
        return f'Subscription <{self.id}> on {self.date}'
