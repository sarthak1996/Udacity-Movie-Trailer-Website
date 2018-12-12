from video import Video
from media import Anime, Movie, Series


def read_data(file_name):
    content = ''
    with f as open(file_name, 'r'):
        content = f.read()
    return content


def write_data(file_name, mode, content):
    with f as open(file_name, mode):
        f.write(content)
    return 1


def update_entry(file_name, videos, video_index, new_video_entry):
    video[video_index] = new_video_entry
    write_data(file_name, 'w', video.convert_to_xml())
    return 1
