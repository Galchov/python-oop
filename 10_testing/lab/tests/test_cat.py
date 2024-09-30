from unittest import TestCase, main

from projects.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        # Arrange: Create 'Cat' instance to use in multiple tests
        self.cat = Cat("Garfield")

    def test_init(self):
        # Assert: Check if attributes are attached correctly
        self.assertEqual("Garfield", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat__the_cat_is_fed__raises(self):
        # Arrange: Setting up the necessary conditions for the test
        self.cat.fed = True

        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        # Act: Attempt to feed the cat after it's already done
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        # Assert: Check if the attributes have changed as expected and
        # the correct message is displayed
        self.assertEqual("Already fed.", str(ex.exception))
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat__the_cat_is_not_fed__changes_state(self):
        # Act: Attempt to eat as the cat is not fed yet
        self.cat.eat()

        # Assert: Check if the cat state has changed
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1, self.cat.size)

    def test_sleep__the_cat_is_not_fed__raises(self):
        # Act: Attempt to sleep without eating
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        # Assert: Check if the state has changed and correct message is displayed
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_sleep__the_cat_is_fed__changes_state(self):
        # Arrange: Set the 'fed' and 'sleepy' attributes to True for the test
        self.cat.fed = True
        self.cat.sleepy = True

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        # Act: Call the method 'sleep' as 'fed = True'
        self.cat.sleep()

        # Assert: Check if the state has changed
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
