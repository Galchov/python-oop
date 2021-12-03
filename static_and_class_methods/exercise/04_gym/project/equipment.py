class Equipment:
    __id = 1

    def __init__(self, name: str):
        self.name = name
        self.id = Equipment.__assign_next_id()

    @classmethod
    def __assign_next_id(cls):
        next_id = Equipment.__id
        Equipment.__id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Equipment.__id

    def __repr__(self):
        return f'Equipment <{self.id}> {self.name}'
