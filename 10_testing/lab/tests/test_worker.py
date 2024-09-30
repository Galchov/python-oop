from unittest import TestCase, main

from projects.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        # Arrange: Create a 'Worker' instance for use in multiple tests
        self.worker = Worker("Test", 1000, 50)

    def test_init(self):
        # Assert: Check if attributes are attached correctly
        self.assertEqual("Test", self.worker.name)
        self.assertEqual(1000, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work__worker_has_zero_energy__raises(self):
        # Arrange: Setting up necessary conditions for the test
        self.worker.energy = 0
        self.worker.money = 0

        # Act: Attempting to work with zero energy should raise Exception
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        # Assert: Check if the 'Exception' is raised and 'energy' and 'money' remain the same
        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(0, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work__worker_has_energy_negative_number__raises(self):
        # Arrange: Setting up necessary conditions for the test
        self.worker.energy = -1
        self.worker.money = 0

        # Act: Attempting to work with zero energy should raise Exception
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        # Assert: Check if the 'Exception' is raised and 'energy' and 'money' remain the same
        self.assertEqual("Not enough energy.", str(ex.exception))
        self.assertEqual(-1, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work__worker_has_energy_positive_number__changes_state(self):
        # Act: Calling the 'work' method with all necessary resources
        self.worker.work()

        # Assert: Check if the expected changes to 'money' and 'energy' are commited
        self.assertEqual(1000, self.worker.money)
        self.assertEqual(49, self.worker.energy)

    def test_rest__increases_energy(self):
        # Act: Call the 'rest' method to increase the energy
        self.worker.rest()

        # Assert: Check if the worker's energy has increased after the rest
        self.assertEqual(51, self.worker.energy)

    def test_get_info__expects_valid_string(self):
        # Act: Get the result from 'get_info' method
        result = self.worker.get_info()

        # Assert: Check if the method will return the expected result
        name = self.worker.name
        money = self.worker.money
        self.assertEqual(f'{name} has saved {money} money.', self.worker.get_info())


if __name__ == "__main__":
    main()
