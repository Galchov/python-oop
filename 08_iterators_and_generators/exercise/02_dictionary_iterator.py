from typing import Dict


class dictionary_iter:
    def __init__(self, dict_obj: Dict) -> None:
        self.dict_obj_tuple = tuple(dict_obj.items())
        self.current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_index < len(self.dict_obj_tuple):
            current_index = self.current_index
            self.current_index += 1
            return self.dict_obj_tuple[current_index]
        raise StopIteration


# Test code:
print("----- Test 1 -----")
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

print()
print("----- Test 2 -----")
result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

