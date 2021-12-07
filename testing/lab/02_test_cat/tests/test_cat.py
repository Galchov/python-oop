"""
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
"""
from project.cat import Cat

import unittest


class CatTests(unittest.TestCase):
    valid_name = 'Tom'

    # Arrange for ALL the tests:
    def setUp(self):
        self.cat = Cat(self.valid_name)

    def test_cat_eat__when_valid__expect_cat_size_to_increase(self):
        """Cat's size is increased after eating"""

        # Act:
        self.cat.eat()

        # Assert:
        self.assertEqual(1, self.cat.size)

    def test_cat_eat__when_cat_is_fed__expect_fed_to_be_true(self):
        """Cat is fed after eating, self.fed = True"""
        # Act:
        self.cat.eat()

        # Assert:
        self.assertTrue(self.cat.fed)

    def test_eat__when_cat_fed_is_true__expect_error(self):
        """Cat cannot eat if it is already fed, raise an error"""
        # Arrange:
        self.cat.eat()

        with self.assertRaises(Exception):
            self.cat.eat()

    def test_sleep__when_cat_not_fed_cannot_fall_asleep__expect_error(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        with self.assertRaises(Exception):
            self.cat.sleep()

    def test_sleepy__when_cat_had_sleep__expect_error(self):
        """Cat is not sleepy after sleeping"""
        # Act:
        self.cat.eat()
        self.cat.sleep()

        # Assert:
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
