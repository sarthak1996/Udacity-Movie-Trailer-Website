from video import Video


class Movie(Video):

    def __init__(self, movie_title=None, movie_storyline=None, movie_poster=None, movie_trailer=None, movie_duration=0):
        Video.__init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_duration)
        self.type = 'M'

    def print_formatted_output(self):
        print('\n\n')
        print('Movie'.center(self.disp_size, ':'))
        Video.print_formatted_output(self)


class Series(Video):

    def __init__(self, series_title=None, series_storyline=None, series_poster=None, series_trailer=None, series_duration=0):
        Video.__init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration)
        self.type = 'S'

    def print_formatted_output(self):
        print('\n\n')
        print('Series'.center(self.disp_size, ':'))
        Video.print_formatted_output(self)


class Anime(Video):

    def __init__(self, anime_title=None, anime_storyline=None, anime_poster=None, anime_trailer=None, anime_duration=0):
        Video.__init__(self, anime_title, anime_storyline, anime_poster, anime_trailer, anime_duration)
        self.type = 'A'

    def print_formatted_output(self):
        print('\n\n')
        print('Anime'.center(self.disp_size, ':'))
        Video.print_formatted_output(self)
