from unittest import TestCase, main

from project.hero import Hero


class HeroTests(TestCase):
    TEST_USERNAME = 'Username'
    TEST_LEVEL = 10
    TEST_HEALTH = 100
    TEST_DAMAGE = 40

    def setUp(self) -> None:
        self.hero = Hero(self.TEST_USERNAME, self.TEST_LEVEL, self.TEST_HEALTH, self.TEST_DAMAGE)
        self.enemy_hero = Hero(username='Enemy', level=8, health=100, damage=30)

    def test_init__expect_to_set_correct_values(self):
        self.assertEqual(self.TEST_USERNAME, self.hero.username)
        self.assertEqual(self.TEST_LEVEL, self.hero.level)
        self.assertEqual(self.TEST_HEALTH, self.hero.health)
        self.assertEqual(self.TEST_DAMAGE, self.hero.damage)

    def test_battle__when_your_and_enemy_names_match__expect_exception(self):
        self.enemy_hero.username = 'Username'
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_your_health_is_less_or_equal_to_zero__expect_value_error(self):
        self.hero.health = -5
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_enemy_health_is_less_or_equal_to_zero__expect_value_error(self):
        self.enemy_hero.health = -5
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy_hero)

        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(context.exception))

    def test_battle__when_both_healths_are_equal_or_less_than_zero__expect_draw(self):
        self.hero.damage = 120
        self.enemy_hero.damage = 110

        expected_message = 'Draw'
        result = self.hero.battle(self.enemy_hero)

        self.assertEqual(expected_message, result)

    def test_battle__when_enemy_health_is_less_or_equal_to_zero__expect_win(self):
        self.hero.health = 300
        self.hero.damage = 120
        expected_message = 'You win'

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_message, result)
        self.assertEqual(65, self.hero.health)
        self.assertEqual(125, self.hero.damage)
        self.assertEqual(11, self.hero.level)

    def test_battle__when_your_health_is_less_or_equal_to_zero__expect_to_lose(self):
        self.enemy_hero.health = 500
        self.enemy_hero.damage = 120
        expected_message = 'You lose'

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(expected_message, result)
        self.assertEqual(105, self.enemy_hero.health)
        self.assertEqual(125, self.enemy_hero.damage)
        self.assertEqual(9, self.enemy_hero.level)

    def test_str__expect_correct_return(self):
        expected_message = f'''Hero {self.hero.username}: {self.hero.level} lvl
Health: {self.hero.health}
Damage: {self.hero.damage}
'''

        self.assertEqual(expected_message, self.hero.__str__())


if __name__ == '__main__':
    unittest.main()
