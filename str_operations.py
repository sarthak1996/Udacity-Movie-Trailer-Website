def fit_string_to_width(param_str, width, enable_hyphen=False):
    i = 0
    str_split = []
    while(i < len(param_str)):
        if not(enable_hyphen):
            str_split.append(param_str[i:i + width])
            i += width
        else:
            tmp_str = param_str[i:i + width]
            i = i + width
            if tmp_str[-1] != ' ' and i < len(param_str):
                tmp_str = list(tmp_str)
                if tmp_str[-2] != ' ':
                    tmp_str[-1] = '-'
                else:
                    tmp_str[-1] = ' '
                tmp_str = ''.join(tmp_str)
                i -= 1
            str_split.append(tmp_str)
    return str_split


def get_str_left_allign(self, param_str):
    l_padding = 0
    for i in param_str:
        l_padding += 1
        if i == ':':
            break
    return l_padding


def convert_line_breaks_to_strs(self, param_str):
    return param_str.split('\n')
