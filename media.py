from video import Video


class Movie(Video):
    '''
    XML TAGS
    '''
    MOVIE_TAG = '<movie>{content}</movie>\n'

    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_duration=0):
        Video.__init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_duration)

    def __init__(self):
        Video.__init__(self)

    def convert_to_xml(self):
        return Video.convert_to_xml(self, self.MOVIE_TAG)


class Series(Video):
    '''
    XML TAGS
    '''
    SERIES_TAG = '<series>{content}</series>\n'

    def __init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration=0):
        Video.__init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration)

    def __init__(self):
        Video.__init__(self)

    def convert_to_xml(self):
        return Video.convert_to_xml(self, self.SERIES_TAG)


class Anime(Video):
    '''
    XML TAGS
    '''
    ANIME_TAG = '<anime>{content}</anime>\n'

    def __init__(self, anime_title, anime_storyline, anime_poster, anime_trailer, anime_duration=0):
        Video.__init__(self, anime_title, anime_storyline, anime_poster, anime_trailer, anime_duration)

    def __init__(self):
        Video.__init__(self)

    def convert_to_xml(self):
        return Video.convert_to_xml(self, self.ANIME_TAG)
