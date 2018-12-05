import webbrowser
from video import Video


class Movie(Video):
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_duration=0):
        Video.__init__(self, movie_title, movie_storyline, movie_duration)
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Series(Video):
    def __init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration=0):
        Video.__init__(self, series_title, series_storyline, series_duration)
        self.poster_image_url = series_poster
        self.trailer_youtube_url = series_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


class Anime(Video):
    def __init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration=0):
        Video.__init__(self, series_title, series_storyline, series_duration)
        self.poster_image_url = series_poster
        self.trailer_youtube_url = series_trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
