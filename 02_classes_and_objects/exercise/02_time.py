class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        return f"%02d:%02d:%02d" % (self.hours, self.minutes, self.seconds)

    def next_second(self):
        total_seconds = (self.hours * 3600) + (self.minutes * 60) + self.seconds
        next_time = total_seconds + 1
        self.hours = next_time // 3600
        self.minutes = (next_time % 3600) // 60
        self.seconds = next_time % 60

        if self.hours > Time.max_hours:
            self.hours = 0
        if self.minutes > Time.max_minutes:
            self.minutes = 0
        if self.seconds > Time.max_seconds:
            self.seconds = 0

        return self.get_time()


# Test code:
time = Time(23, 59, 59)
print(time.next_second())
