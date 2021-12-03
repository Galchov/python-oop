class Customer:
    __id = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.__assign_next_id()

    @classmethod
    def __assign_next_id(cls):
        next_id = Customer.__id
        Customer.__id += 1
        return next_id

    @staticmethod
    def get_next_id():
        return Customer.__id

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'
