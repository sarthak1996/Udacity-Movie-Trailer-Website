class Video():
    comments = None

    def __init__(self, title, storyline, duration=0):
        self.title = title
        self.duration = duration
        self.storyline = storyline

    def get_title(self):
        return self.title

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def set_title(self, title):
        self.title = title

    def set_storyline(self, storyline):
        self.storyline = storyline

    def get_storyline(self):
        return self.storyline

    def get_comments(self):
        return self.comments

    def set_comments(self, comments):
        self.comments = comments

    def add_comment(self, comment):
        if self.comments is None:
            self.comments = []
        self.comments.append(comment)

    def has_comments(self):
        return not(self.comments is None)

    def convert_to_xml(self):
        content = '  <title>' + self.title + '</title>\n'
        content += '  <storyline>' + self.storyline + '</storyline>\n'
        content += '  <duration>' + str(self.duration) + '</duration>\n'
        return content
