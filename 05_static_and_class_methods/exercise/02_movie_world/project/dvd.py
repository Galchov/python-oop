class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @staticmethod
    def get_month_name(month_number: int) -> str:
        months = {1: "January",
                  2: "February",
                  3: "March",
                  4: "April",
                  5: "May",
                  6: "June",
                  7: "July",
                  8: "August",
                  9: "September",
                  10: "October",
                  11: "November",
                  12: "December",
                  }

        return months[month_number]

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int) -> "DVD":
        day, month, year = [int(el) for el in date.split('.')]
        month_name = cls.get_month_name(month)
        # Or just 'from calendar import month_name', but I wasn't lazy to write a method
        return cls(name, id, year, month_name, age_restriction)

    def __repr__(self) -> str:
        rent_status = "rented" if self.is_rented else "not rented"
        return (f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has "
                f"age restriction {self.age_restriction}. Status: {rent_status}")
