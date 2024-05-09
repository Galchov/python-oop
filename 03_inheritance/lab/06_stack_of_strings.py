class Stack:
    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop(-1)

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not self.data

    def __str__(self):
        stack_reversed = reversed(self.data)
        print_data = ", ".join(stack_reversed)
        return f"[{print_data}]"
