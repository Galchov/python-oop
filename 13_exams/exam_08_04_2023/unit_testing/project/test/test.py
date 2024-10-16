from unittest import TestCase, main

from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player_1 = TennisPlayer("Dimitrov", 33, 3580)
        self.player_2 = TennisPlayer("Djokovic", 37, 6210)
        self.player_3 = TennisPlayer("Humbert", 26, 2515)

    def test_init(self):
        self.assertEqual("Dimitrov", self.player_1.name)
        self.assertEqual(33, self.player_1.age)
        self.assertEqual(3580, self.player_1.points)
        self.assertEqual([], self.player_1.wins)

    def test_name_setter__name_shorter_than_2__raises_error(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("Di", 33, 3580)
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_setter__player_age_under_18__raises_error(self):
        with self.assertRaises(ValueError) as ex:
            TennisPlayer("Dimitrov", 17, 3580)
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win__tournament_not_in__adds_tournament(self):
        actual = self.player_1.add_new_win("Wimbledon 2024")
        self.assertEqual(["Wimbledon 2024"], self.player_1.wins)
        self.assertIsNone(actual)

    def test_add_new_win__tournament_already_in__returns_message(self):
        self.player_1.add_new_win("Wimbledon 2024")
        actual = self.player_1.add_new_win("Wimbledon 2024")
        self.assertEqual("Wimbledon 2024 has been already added to the list of wins!", actual)

    def test_lt__other_player_is_better__return_appropriate_message(self):
        actual = self.player_1 < self.player_2
        self.assertEqual("Djokovic is a top seeded player and he/she is better than Dimitrov", actual)

    def test_lt__self_player_is_better__return_appropriate_message(self):
        actual = self.player_1 < self.player_3
        self.assertEqual("Dimitrov is a better player than Humbert", actual)

    def test_str__no_wins__return_message_without_them(self):
        actual = str(self.player_1)
        expected = "Tennis Player: Dimitrov\nAge: 33\nPoints: 3580.0\nTournaments won: "
        self.assertEqual(expected, actual)

    def test_str__player_has_wins__return_message_with_them(self):
        self.player_1.add_new_win("Wimbledon 2024")
        self.player_1.add_new_win("Australia Open 2023")
        actual = str(self.player_1)
        expected = ("Tennis Player: Dimitrov\nAge: 33\nPoints: 3580.0\n"
                    "Tournaments won: Wimbledon 2024, Australia Open 2023")
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
