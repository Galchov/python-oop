from project.id_mixin import IDMixin


class ExercisePlan(IDMixin):
    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration
        self.id = self.get_next_id()

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int) -> "ExercisePlan":
        duration_minutes = hours * 60
        return cls(trainer_id, equipment_id, duration_minutes)

    def __repr__(self) -> str:
        return f"Plan <{self.id}> with duration {self.duration} minutes"
