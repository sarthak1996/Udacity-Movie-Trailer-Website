import webbrowser
from video import Video


class Movie(Video):
    def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer, movie_duration=0):
        Video.__init__(self, movie_title, movie_storyline, movie_duration)
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def __init__(self):
        Video.__init__(self)
        self.poster_image_url = None
        self.trailer_youtube_url = None

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def convert_to_xml(self):
        content = '\n<movie>\n'
        content += Video.convert_to_xml(self)
        content += '  <poster_image_url>' + self.poster_image_url.replace('</', '').replace('>', '') + '</poster_image_url>\n'
        content += '  <trailer_youtube_url>' + self.trailer_youtube_url.replace('</', '').replace('>', '') + '</trailer_youtube_url>\n'
        content += '</movie>'
        return content


class Series(Video):
    def __init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration=0):
        Video.__init__(self, series_title, series_storyline, series_duration)
        self.poster_image_url = series_poster
        self.trailer_youtube_url = series_trailer

    def __init__(self):
        Video.__init__(self)
        self.poster_image_url = None
        self.trailer_youtube_url = None

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def convert_to_xml(self):
        content = '\n<series>\n'
        content += Video.convert_to_xml(self)
        content += '  <poster_image_url>' + self.poster_image_url.replace('</', '').replace('>', '') + '</poster_image_url>\n'
        content += '  <trailer_youtube_url>' + self.trailer_youtube_url.replace('</', '').replace('>', '') + '</trailer_youtube_url>\n'
        content += '</series>'
        return content


class Anime(Video):
    def __init__(self, series_title, series_storyline, series_poster, series_trailer, series_duration=0):
        Video.__init__(self, series_title, series_storyline, series_duration)
        self.poster_image_url = series_poster
        self.trailer_youtube_url = series_trailer

    def __init__(self):
        Video.__init__(self)
        self.poster_image_url = None
        self.trailer_youtube_url = None

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def convert_to_xml(self):
        content = '\n<anime>\n'
        content += Video.convert_to_xml(self)
        content += '  <poster_image_url>' + self.poster_image_url.replace('</', '').replace('>', '') + '</poster_image_url>\n'
        content += '  <trailer_youtube_url>' + self.trailer_youtube_url.replace('</', '').replace('>', '') + '</trailer_youtube_url>\n'
        content += '</anime>'
        return content
