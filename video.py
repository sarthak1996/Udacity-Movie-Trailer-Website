import webbrowser


class Video():
    comments = None
    attrs = {0: 'title', 1: 'storyline', 2: 'duration', 3: 'poster_image_url', 4: 'trailer_youtube_url'}

    '''
    XML tags
    '''
    TITLE_TAG = '    <title>{content}</title>\n'
    STORYLINE_TAG = '    <storyline>{content}</storyline>\n'
    DURATION_TAG = '    <duration>{content}</duration>\n'
    POSTER_URL_TAG = '    <poster>{content}</poster>\n'
    TRAILER_TAG = '    <trailer>{content}</trailer>\n'
    '''
    '''

    def __init__(self, title, storyline, poster, trailer, duration=0):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def __init__(self):
        self.title = None
        self.duration = 0
        self.storyline = None
        self.poster_image_url = None
        self.trailer_youtube_url = None

    def add_comment(self, comment):
        if self.comments is None:
            self.comments = []
        self.comments.append(comment)

    def has_comments(self):
        return not(self.comments is None)

    def convert_to_xml(self, container_tag):
        content = self.TITLE_TAG.format(content=self.title)
        content += self.STORYLINE_TAG.format(content=self.storyline)
        content += self.DURATION_TAG.format(content=self.duration)
        content += self.POSTER_URL_TAG.format(content=self.poster_image_url)
        content += self.TRAILER_TAG.format(content=self.trailer_youtube_url)
        content = container_tag.format(content=content)
        return content

    def get_attrs_string(self):
        return self.attrs

    def get_attr(self, attr_index):
        if attr_index == 0:
            return self.title
        elif attr_index == 1:
            return self.storyline
        elif attr_index == 2:
            return self.duration
        elif attr_index == 3:
            return self.poster_image_url
        elif attr_index == 4:
            return self.trailer_youtube_url

    def set_attr_value(self, attr_index, value):
        if attr_index == 0:
            self.title = value
        elif attr_index == 1:
            self.storyline = value
        elif attr_index == 2:
            self.duration = value
        elif attr_index == 3:
            self.poster_image_url = value
        elif attr_index == 4:
            self.trailer_youtube_url = value
        else:
            print('Atrb exists but update method is not defined for it!')
            return -1
        return 1

    def set_attr(self, attr_indices, upd_video_obj):
        for chosen_attr in attr_indices:
            if chosen_attr in self.attrs:
                if (self.set_attr_value(self, chosen_attr, upd_video_obj.get_attr(self, chosen_attr))) == -1:
                    return -1
            else:
                print('ERROR: Entered index is not a valid index for attribute!')
                return -1
        return self

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def print_formatted_attrs(self):
        print(self.attrs)

    def validate_attr_list(self, attr_indices):
        for index in attr_indices:
            if index not in self.attrs:
                return False
        return True

    def input_attr_values(self):
        print()
