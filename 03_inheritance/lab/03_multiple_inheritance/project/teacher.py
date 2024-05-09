from project.person import Person
from project.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


# Test code:
teacher = Teacher()
print(teacher.teach())
print(teacher.sleep())
print(teacher.get_fired())

"""
An example of Multiple Inheritance - When a child class inherits from 
more than one parent classes.
"""
