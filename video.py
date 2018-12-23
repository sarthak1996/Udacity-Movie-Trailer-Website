import webbrowser
<<<<<<< HEAD
import str_operations
import urllib.request
=======
import textwrap
import str_operations
>>>>>>> 88dc2fb027ece15b28c6c53095dc50a729b71f47


class Video():
    comments = None
    attrs = {0: 'title', 1: 'storyline', 2: 'duration', 3: 'poster_image_url', 4: 'trailer_youtube_url'}
    attrs_display_names = ['Title', 'Storyline', 'Duration', 'Poster Image link', 'Trailer youtube link']
    disp_size = 70

    '''
    ATTRIBUTE INDEX_NUM
    '''
    ATTR_INDEX_TITLE = 0
    ATTR_INDEX_STORYLINE = 1
    ATTR_INDEX_DURATION = 2
    ATTR_INDEX_POSTER_IMAGE_URL = 3
    ATTR_INDEX_TRAILER_YOUTUBE_URL = 4
<<<<<<< HEAD

    '''
    INPUT VALIDATION MESSAGES
    '''
    ERR_INV_TITLE = 1
    ERR_INV_STORY_LINE = 2
    ERR_INV_DURATION = 3
    ERR_INV_POSTER = 4
    ERR_INV_TRAILER = 5
    INV_SUCCESS = 6
    INV_GENERIC_ERROR = 7

=======

    '''
    INPUT VALIDATION MESSAGES
    '''
    ERR_INV_TITLE = 1
    ERR_INV_STORY_LINE = 2
    ERR_INV_DURATION = 3
    ERR_INV_POSTER = 4
    ERR_INV_TRAILER = 5
    INV_SUCCESS = 6
    INV_GENERIC_ERROR = 7

>>>>>>> 88dc2fb027ece15b28c6c53095dc50a729b71f47
    def __init__(self, title, storyline, poster, trailer, duration=0):
        self.title = title
        self.duration = duration
        self.storyline = storyline
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer

    def add_comment(self, comment):
        if self.comments is None:
            self.comments = []
        self.comments.append(comment)

    def has_comments(self):
        return not(self.comments is None)

    def get_attrs_string(self):
        return self.attrs

<<<<<<< HEAD
    def get_comments(self):
        return self.comments

    def get_attr(self, attr_index):
        if attr_index == self.ATTR_INDEX_TITLE:
            return self.title
        elif attr_index == self.ATTR_INDEX_STORYLINE:
            return self.storyline
        elif attr_index == self.ATTR_INDEX_DURATION:
            return self.duration
        elif attr_index == self.ATTR_INDEX_POSTER_IMAGE_URL:
            return self.poster_image_url
        elif attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
            return self.trailer_youtube_url

    def set_attr_value(self, attr_index, value):
        if attr_index == self.ATTR_INDEX_TITLE:
            self.title = value
        elif attr_index == self.ATTR_INDEX_STORYLINE:
            self.storyline = value
        elif attr_index == self.ATTR_INDEX_DURATION:
            self.duration = value
        elif attr_index == self.ATTR_INDEX_POSTER_IMAGE_URL:
            self.poster_image_url = value
        elif attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
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

=======
    def get_attr(self, attr_index):
        if attr_index == self.ATTR_INDEX_TITLE:
            return self.title
        elif attr_index == self.ATTR_INDEX_STORYLINE:
            return self.storyline
        elif attr_index == self.ATTR_INDEX_DURATION:
            return self.duration
        elif attr_index == self.ATTR_INDEX_POSTER_IMAGE_URL:
            return self.poster_image_url
        elif attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
            return self.trailer_youtube_url

    def set_attr_value(self, attr_index, value):
        if attr_index == self.ATTR_INDEX_TITLE:
            self.title = value
        elif attr_index == self.ATTR_INDEX_STORYLINE:
            self.storyline = value
        elif attr_index == self.ATTR_INDEX_DURATION:
            self.duration = value
        elif attr_index == self.ATTR_INDEX_POSTER_IMAGE_URL:
            self.poster_image_url = value
        elif attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
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

>>>>>>> 88dc2fb027ece15b28c6c53095dc50a729b71f47
    def validate_input_attr_value(self, attr_index, attr_input_value):
        if attr_index == self.ATTR_INDEX_TITLE:
            # title
            if attr_input_value is not None and attr_input_value != '':
                return self.INV_SUCCESS
            return self.ERR_INV_TITLE
        elif attr_index == self.ATTR_INDEX_STORYLINE:
            # storyline
            return self.INV_SUCCESS
        elif attr_index == self.ATTR_INDEX_DURATION:
            # duration
            try:
<<<<<<< HEAD
                float(attr_input_value)
=======
                _ = float(attr_input_value)
>>>>>>> 88dc2fb027ece15b28c6c53095dc50a729b71f47
            except:
                return self.ERR_INV_DURATION
            return self.INV_SUCCESS
        elif attr_index == self.ATTR_INDEX_POSTER_IMAGE_URL:
            # poster image
<<<<<<< HEAD
            try:
                if urllib.request.urlopen(attr_input_value).code == 200:
                    return self.INV_SUCCESS
            except:
                return self.ERR_INV_POSTER
            return self.ERR_INV_POSTER
        elif attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
            if 'youtube' not in attr_input_value:
                return self.ERR_INV_TRAILER
            try:
                if urllib.request.urlopen(attr_input_value).code == 200:
                    return self.INV_SUCCESS
            except:
                return self.ERR_INV_TRAILER
            return self.ERR_INV_TRAILER

    def print_validation_error(self, attr_index):
        if attr_index == self.ATTR_INDEX_TITLE:
            print('ERROR: Title can not be empty!')
        if attr_index == self.ATTR_INDEX_STORYLINE:
            print('No validations on storyline! Safe to continue')
        if attr_index == self.ATTR_INDEX_DURATION:
            print('ERROR: Duration must be a float or int!')
        if attr_index == self.ATTR_INDEX_POSTER_IMAGE_URL:
            print('ERROR: Did not receive a success response when hitting the url')
            print('PS: Include https://')
        if attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
            print('ERROR: Either the url does not contain youtube or did not receive a success response when hitting the url')
            print('PS: Include https://')
=======
            return self.INV_SUCCESS
        elif attr_index == self.ATTR_INDEX_TRAILER_YOUTUBE_URL:
            if 'youtube' not in attr_input_value:
                return self.ERR_INV_TRAILER
            return self.INV_SUCCESS

    def print_validation_error(self, attr_index):
        print('Error validating:' + str(attr_index))
>>>>>>> 88dc2fb027ece15b28c6c53095dc50a729b71f47

    def input_attr_values(self, type, attr_update=False, attr_index=None):
        validation_status = self.INV_GENERIC_ERROR
        val1, val2, val3, val4, val5 = 'Random title', None, 0, None, None
        while(validation_status != self.INV_SUCCESS):
            val1 = input('Enter ' + type + ' title:')
            validation_status = self.validate_input_attr_value(self.ATTR_INDEX_TITLE, val1)
            if validation_status != self.INV_SUCCESS:
                self.print_validation_error(self.ATTR_INDEX_TITLE)
        validation_status = self.INV_GENERIC_ERROR
        while(validation_status != self.INV_SUCCESS):
            val2 = input('Enter ' + type + ' storyline:')
            validation_status = self.validate_input_attr_value(self.ATTR_INDEX_STORYLINE, val2)
            if validation_status != self.INV_SUCCESS:
                self.print_validation_error(self.ATTR_INDEX_STORYLINE)
        validation_status = self.INV_GENERIC_ERROR
        while(validation_status != self.INV_SUCCESS):
            val3 = input('Enter ' + type + ' duration:')
            validation_status = self.validate_input_attr_value(self.ATTR_INDEX_DURATION, val3)
            if validation_status != self.INV_SUCCESS:
                self.print_validation_error(self.ATTR_INDEX_DURATION)
        validation_status = self.INV_GENERIC_ERROR
        while(validation_status != self.INV_SUCCESS):
            val4 = input('Enter ' + type + "'s poster image link:")
            validation_status = self.validate_input_attr_value(self.ATTR_INDEX_POSTER_IMAGE_URL, val4)
            if validation_status != self.INV_SUCCESS:
                self.print_validation_error(self.ATTR_INDEX_POSTER_IMAGE_URL)
        validation_status = self.INV_GENERIC_ERROR
        while(validation_status != self.INV_SUCCESS):
            val5 = input('Enter ' + type + "'s trailer youtube link:")
            validation_status = self.validate_input_attr_value(self.ATTR_INDEX_TRAILER_YOUTUBE_URL, val5)
            if validation_status != self.INV_SUCCESS:
                self.print_validation_error(self.ATTR_INDEX_TRAILER_YOUTUBE_URL)
        self.set_attr_value(self.ATTR_INDEX_TITLE, val1)
        self.set_attr_value(self.ATTR_INDEX_STORYLINE, val2)
        self.set_attr_value(self.ATTR_INDEX_DURATION, val3)
        self.set_attr_value(self.ATTR_INDEX_POSTER_IMAGE_URL, val4)
        self.set_attr_value(self.ATTR_INDEX_TRAILER_YOUTUBE_URL, val5)
        return self

    def update_video_attrs(self, video_type, attr_indices):

        print('Updating {type} attributes'.format(type=video_type))
        for attr_index in attr_indices:
            validation_status = self.INV_GENERIC_ERROR
            print(self.attrs)
            print(self.attrs.get(0))
            print(attr_index)
            while(validation_status != self.INV_SUCCESS):
                val = input('Enter {type} {attr_name} :'.format(type=video_type, attr_name=self.attrs.get(attr_index)))
                validation_status = self.validate_input_attr_value(attr_index, val)
                print('here!')
                print(validation_status)
            self.set_attr_value(attr_index, val)
        return

    def print_formatted_output(self):
        print('*' * self.disp_size)
        print(str_operations.convert_values_to_fit_display('Title:', self.title, self.disp_size, enable_hyphen=True))
        print()
        print(str_operations.convert_values_to_fit_display('Storyline:', self.storyline, self.disp_size, enable_hyphen=True))
        print()
        print(str_operations.convert_values_to_fit_display('Duration:', self.duration, self.disp_size, enable_hyphen=True))
        print()
        print(str_operations.convert_values_to_fit_display('Poster:', self.poster_image_url, self.disp_size, enable_hyphen=True))
        print()
        print(str_operations.convert_values_to_fit_display('Trailer:', self.trailer_youtube_url, self.disp_size, enable_hyphen=True))
        print()
        print('*' * self.disp_size)
<<<<<<< HEAD

    def initialize_undefined_vals(self):
        if self.storyline is None or self.storyline == '':
            self.storyline = 'No description available'
        if self.poster_image_url is None or self.poster_image_url is '':
            self.poster_image_url = 'https://avatars3.githubusercontent.com/u/1785581?s=88&v=4'

    def escape_chars(self):
        self.title = self.title.replace('"', '\'')
        self.storyline = self.storyline.replace('"', '\'')
        self.poster_image_url = self.poster_image_url.replace('"', '\'')
        self.trailer_youtube_url = self.trailer_youtube_url.replace('"', '\'')
=======

    def initialize_undefined_vals(self):
        if self.storyline is None or self.storyline == '':
            self.storyline = 'No description available'
        if self.poster_image_url is None or self.poster_image_url is '':
            self.poster_image_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBBzFzubK-Pjf3RXpLSSG5Ujb4hxZxaA65uoo7qFSBFwKOO-jT'
>>>>>>> 88dc2fb027ece15b28c6c53095dc50a729b71f47
