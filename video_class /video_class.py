class Video:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
        self.position = 0

    def play(self):
        print("Playing")

    def advance(self, minutes):
        self.position = min(self.position + minutes, self.duration)

    def is_finished(self):
        return self.position >= self.duration

    def restart(self):
        self.position = 0

    def time_remaining(self):
        return self.duration - self.position