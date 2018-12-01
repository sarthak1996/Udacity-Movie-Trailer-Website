class Video():
    def __init__(self):
        self.title = ''
        self.duration = 0
        self.storyline=''

    def __init__(self, title, duration,storyline):
        self.title = title
        self.duration = duration
        self.storyline=storyline

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration()

    def set_duration(self, duration):
        self.duration = duration

    def set_title(self, title):
        self.title = title

    def set_storyline(self, storyline):
        self.storyline = storyline

    def get_storyline(self):
        return seld.storyline
