from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    @property
    def team_financial_data(self):
        expenses_per_race = 250_000
        sponsors = {
            "Oracle": {1: 1_500_000, 2: 800_000},
            "Honda": {8: 20_000, 10: 10_000},
                    }

        return expenses_per_race, sponsors
