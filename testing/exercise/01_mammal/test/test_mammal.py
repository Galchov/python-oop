from unittest import TestCase, main

from project.mammal import Mammal


class MammalTests(TestCase):
    VALID_TEST_NAME = 'Mammal'
    VALID_TEST_TYPE = 'type 1'
    VALID_TEST_SOUND = 'some sound'

    def setUp(self) -> None:
        self.mammal = Mammal(self.VALID_TEST_NAME, self.VALID_TEST_TYPE, self.VALID_TEST_SOUND)

    def test_init__expect_to_set_correct_values(self):
        self.assertEqual(self.VALID_TEST_NAME, self.mammal.name)
        self.assertEqual(self.VALID_TEST_TYPE, self.mammal.type)
        self.assertEqual(self.VALID_TEST_SOUND, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound__when_name_and_sound__expect_correct_return(self):
        result = self.mammal.make_sound()

        self.assertEqual(f"{self.VALID_TEST_NAME} makes {self.VALID_TEST_SOUND}", result)

    def test_get_kingdom__expect_to_return_correct_result(self):
        result = self.mammal.get_kingdom()

        self.assertEqual("animals", result)

    def test_info__expect_to_return_correct_result(self):
        result = self.mammal.info()

        self.assertEqual(f"{self.VALID_TEST_NAME} is of type {self.VALID_TEST_TYPE}", result)


if __name__ == '__main__':
    unittest.main()
