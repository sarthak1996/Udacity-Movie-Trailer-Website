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


def get_str_left_allign(param_str):
    l_padding = 0
    for i in param_str:
        l_padding += 1
        if i == ':':
            break
    return l_padding


def convert_line_breaks_to_strs(param_str):
    return param_str.split('\n')


def convert_values_to_fit_display(param_title, param_value, param_disp_size, enable_hyphen=False):
    param_value = str(param_value)
    l_padding = get_str_left_allign(param_title.center(param_disp_size))
    val_split = fit_string_to_width(param_value, width=param_disp_size - l_padding + 10, enable_hyphen=enable_hyphen)
    if val_split == []:
        val_split = ['']
    param_title += val_split[0]
    param_title = param_title.center(param_disp_size)
    return_str = param_title
    if len(val_split) > 1:
        return_str += '\n'
        return_str += '\n'.join([(' ' * get_str_left_allign(param_title)) + val_split[i] for i in range(1, len(val_split))])
    return return_str
