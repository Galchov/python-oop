class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if isinstance(x, int):
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not isinstance(element, int):
            raise ValueError('Element is not Integer')

        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index not in range(len(self.get_data())):
            raise IndexError('Index is out of range')

        return self.get_data().pop(index)

    def get(self, index):
        if index not in range(len(self.get_data())):
            raise IndexError('Index is out of range')

        return self.get_data().pop(index)

    def insert(self, index, element):
        if index not in range(len(self.get_data())):
            raise IndexError('Index is out of range')
        if not isinstance(element, int):
            raise ValueError('Element is not Integer')

        self.get_data().insert(index, element)
        return self.get_data()

    def get_biggest(self):
        max_value = max(self.get_data())
        return max_value

    def get_index(self, element):
        return self.get_data().index(element)
