class Trainer:
    __id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Trainer.__assign_next_id()

    @classmethod
    def __assign_next_id(cls):
        next_id = Trainer.__id
        Trainer.__id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Trainer.__id

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'
