class IDMixin:
    _id: int = 0

    @classmethod
    def get_next_id(cls):
        cls._id += 1
        return cls._id
