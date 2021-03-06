import unittest
from unittest import TestCase
from person_demo import Person

"""
Example structure of files:

test:
    person:
        # Tests only for VALID validation
        init_valid.py
        # Tests only for INVALID validation
        init_invalid.py
        
        # Tests only for 'get_full_name'
        get_full_name.py
        
        # Tests only for 'get_info'
        get_info.py
"""


class TestPerson(TestCase):
    first_name = 'Test'
    last_name = 'Person'
    age = 7

    # Runs ONCE before ALL tests
    @classmethod
    def setUpClass(cls) -> None:
        print('--- SetUpClass ---')

    # Runs before EACH test
    def setUp(self) -> None:
        print('--- SetUp ---')
        self.person = Person(self.first_name, self.last_name, self.age)

    # Runs after EACH test
    def tearDown(self) -> None:
        print('--- tearDown ---')

    # Runs ONCE after ALL tests
    @classmethod
    def tearDownClass(cls) -> None:
        print('--- tearDownClass ---')

    # Arrange - with_valid_names_and_age
    # Act - get_full_name
    # Assert - valid
    # All three components MUST be in the name of the test

    # def test_getFullName__whenValidNamesAndAge__expectValid(self):
    #             ACT                ARRANGE             ASSERT
    def test_get_full_name__when_valid_names_and_age__expect_valid(self):
        # Arrange
        # first_name = 'Test'
        # last_name = 'Person'
        # age = 7
        # person = Person(first_name, last_name, age)
        # !!!Arrange has been moved to 'setUP' method!!!

        # Act
        actual_full_name = self.person.get_full_name()

        # Assert
        expected_full_name = f'{self.first_name} {self.last_name}'
        # !!! 'expected' to be always FIRST!!!
        self.assertEqual(expected_full_name, actual_full_name)

    def test_get_info__when_valid_names_and_age__expect_valid(self):
        # Arrange
        # first_name = 'Test'
        # last_name = 'Person'
        # age = 7
        # person = Person(first_name, last_name, age)
        # !!!Arrange has been moved to 'setUP' method!!!

        # Act
        actual_info = self.person.get_info()

        # Assert
        expected_info = f'{self.first_name} {self.last_name} is {self.age} years old'
        # !!! 'expected' to be always FIRST!!!
        self.assertEqual(expected_info, actual_info)

    def test_init__when_names_and_age_are_valid__expect_to_create_person(self):
        self.assertEqual(self.first_name, self.person.first_name)
        self.assertEqual(self.last_name, self.person.last_name)
        self.assertEqual(self.age, self.person.age)

    def test_init__when_names_are_valid_age_is_less_than_min__expect_value_exception(self):
        with self.assertRaises(ValueError):
            Person(self.first_name, self.last_name, Person.MIN_AGE - 1)

    def test_init__when_names_are_valid_age_is_greater_than_max__expect_value_exception(self):
        with self.assertRaises(ValueError):
            Person(self.first_name, self.last_name, Person.MAX_AGE + 1)


if __name__ == '__main__':
    unittest.main()
