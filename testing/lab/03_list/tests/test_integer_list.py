from project.integer_list import IntegerList

from unittest import TestCase, main


class TestList(TestCase):
    def setUp(self):
        self.list = IntegerList(1, 2, 3, 4, 5)

    def test_integer_list_init__when_int__expect_to_create_it(self):
        self.assertEqual([1, 2, 3, 4, 5], self.list._IntegerList__data)

    def test_integer_list_init__when_none_is_int__expect_empty_list(self):
        some_list = IntegerList("3", "something")
        self.assertEqual([], some_list._IntegerList__data)

    def test_integer_list_add__when_not_int__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.list.add("something")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_integer_list_add__when_int__expect_to_add_it(self):
        self.list.add(8)
        self.assertEqual([1, 2, 3, 4, 5, 8], self.list._IntegerList__data)

    def test_integer_list_remove__when_invalid_index__expect_exception(self):
        with self.assertRaises(IndexError) as context:
            element = self.list.remove_index(7)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_integer_list_remove__when_valid_index__expect_to_remove_and_return_it(self):
        element = self.list.remove_index(0)
        self.assertEqual(1, element)

    def test_integer_list_get__when_invalid_index__expect_exception(self):
        with self.assertRaises(IndexError) as context:
            element = self.list.get(8)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_integer_list_get__when_valid_index__expect_to_remove_the_item_and_return_it(self):
        element = self.list.get(0)
        self.assertEqual(1, element)

    def test_integer_list_insert__when_not_int__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.list.insert(2, 2.5)
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_integer_list_insert__when_invalid_index__expect_exception(self):
        with self.assertRaises(IndexError) as context:
            self.list.insert(9, 5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_integer_list_insert__when_valid_index_and_element__except_to_insert_it(self):
        self.list.insert(1, 9)
        self.assertEqual([1, 9, 2, 3, 4, 5], self.list._IntegerList__data)

    def test_integer_list_get_biggest__expect_to_return_the_biggest_number(self):
        element = self.list.get_biggest()
        self.assertEqual(5, element)

    def test_integer_list_get_index__expect_to_return_the_element_on_the_given_index(self):
        index = self.list.get_index(2)
        self.assertEqual(1, index)


if __name__ == '__main__':
    main()
