from unittest import TestCase, main

from projects.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        # Arrange: Create 'IntegerList' instance to be used for multiple test
        self.int_list = IntegerList(2, -10, 50, 4, 9)

    def test_init(self):
        # Arrange
        some_list = IntegerList()

        # Assert
        self.assertEqual([], some_list.get_data())

        some_list = IntegerList(2, -10, 50, '@', False)
        self.assertEqual([2, -10, 50], some_list.get_data())

    def test_get_data(self):
        # Act
        result = self.int_list.get_data()

        # Assert: Check if 'get_data' returns the state correctly
        self.assertEqual(self.int_list.get_data(), result)

    def test_add__element_not_int__raises(self):
        self.assertNotIn('100', self.int_list.get_data())

        with self.assertRaises(ValueError) as ex:
            self.int_list.add('100')

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertNotIn('100', self.int_list.get_data())

    def test_add__element_is_integer__appends_and_return(self):
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        result = self.int_list.add(5)

        self.assertIn(5, self.int_list.get_data())
        self.assertEqual([2, -10, 50, 4, 9, 5], result)

    def test_remove_index__larger_than_or_equal_than_len__raises(self):
        # Index equals the length of the list
        # Example that the private attribute can be access by name mangling
        index_to_remove = len(self.int_list.get_data())
        self.assertEqual([2, -10, 50, 4, 9], self.int_list._IntegerList__data)

        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(index_to_remove)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([2, -10, 50, 4, 9], self.int_list._IntegerList__data)

        # Index is larger than the length of the list
        index_to_remove = len(self.int_list.get_data()) + 1
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        with self.assertRaises(IndexError) as ex:
            self.int_list.remove_index(index_to_remove)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

    def test_remove_index__valid_index__removes_element(self):
        self.assertIn(2, self.int_list.get_data())

        result = self.int_list.remove_index(0)

        self.assertNotIn(2, self.int_list.get_data())
        self.assertEqual(2, result)

        self.assertIn(9, self.int_list.get_data())

        result = self.int_list.remove_index(3)
        self.assertNotIn(9, self.int_list.get_data())
        self.assertEqual(9, result)

    def test_get__index_larger_or_equal_than_len__raises(self):
        # Index equal to the len
        index_to_get = len(self.int_list.get_data())

        with self.assertRaises(IndexError) as ex:
            self.int_list.get(index_to_get)

        self.assertEqual("Index is out of range", str(ex.exception))

        # Index is larger
        index_to_get = len(self.int_list.get_data()) + 1

        with self.assertRaises(IndexError) as ex:
            self.int_list.get(index_to_get)

        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get__valid_index__returns_element(self):
        result = self.int_list.get(2)

        self.assertEqual(50, result)

    def test_insert__index_is_larger_or_equal_than_len__raises(self):
        index_to_insert = len(self.int_list.get_data())
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(index_to_insert, 100)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        index_to_insert = len(self.int_list.get_data()) + 1
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        with self.assertRaises(IndexError) as ex:
            self.int_list.insert(index_to_insert, 100)

        self.assertEqual("Index is out of range", str(ex.exception))
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

    def test_insert__valid_index_but_invalid_type__raises(self):
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        with self.assertRaises(ValueError) as ex:
            self.int_list.insert(1, 3.14)

        self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

    def test_insert__valid_index_and_valid_type__inserts_element(self):
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())
        self.int_list.insert(1, 100)
        self.assertEqual([2, 100, -10, 50, 4, 9], self.int_list.get_data())

    def test_get_biggest(self):
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        result = self.int_list.get_biggest()

        self.assertEqual(50, result)
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

    def test_get_index__returns_index(self):
        self.assertEqual([2, -10, 50, 4, 9], self.int_list.get_data())

        result = self.int_list.get_index(4)
        self.assertEqual(3, result)


if __name__ == "__main__":
    main()
