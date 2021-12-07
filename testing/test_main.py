from unittest import TestCase
from main import add


# Inherit TestCase -> to run the tests
class MainTest(TestCase):

    # Test methods MUST start with 'test' (It is 'unittest' library's convention)
    def test_add_when_one_and_two_expect_three(self):
        # Arrange:
        expected = 3

        # Act:
        actual_result = add(1, 2)

        # Assert:
        self.assertEqual(expected, actual_result)

    def test_add_when_two_and_one_expect_three(self):
        expected = 3
        actual_result = add(2, 1)
        self.assertEqual(expected, actual_result)

    def test_add_when_None_and_int_except_exception(self):
        with self.assertRaises(ValueError) as context:
            pass


if __name__ == '__main__':
    unittest.main()
