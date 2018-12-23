import media
import fresh_tomatoes
from video import Video
import sys
from os import system, name

run_mode = 'main'
seeded_videos_allowed = False
seeded_movies_allowed = False
seeded_series_allowed = False
seeded_animes_allowed = False
'''
CONSTANTS START
'''
INV_INPUT = 'Invalid Input'
INPUT_MOVIE_DTLS = 0
INPUT_SERIES_DTLS = 1
INPUT_ANIME_DTLS = 2
PHASE_SEEDED_DECIDE = 'Seeded Videos'
PHASE_VALIDATION = 'Validate added videos'
PHASE_ADD_MOVIE = 'Add Movies'
PHASE_ADD_SERIES = 'Add Series'
PHASE_ADD_ANIME = 'Add Anime'
PHASE_UPD_MOVIES = 'Update Movies'
PHASE_UPD_SERIES = 'Update Series'
PHASE_UPD_ANIME = 'Update Animes'
PHASE_ADD_COMMENTS = 'Add Comments'
PHASE_CONFIRM_END = 'Display Page'
'''
CONSTANTS END
'''

add_num_videos = None
disp_size = 70
curr_add_at = None


def seeded_videos(allowed_movies=True, allowed_series=True, allowed_anime=True):
    pulp_fiction = media.Movie('Pulp Fiction', "In the realm of underworld, a series of incidents intertwines the lives of two Los Angeles mobsters, a gangster's wife, a boxer and two small-time criminals.", 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg', "https://www.youtube.com/watch?v=tGpTpVyI_OQ")

    deadpool = media.Movie('Deadpool', "Mercenary Wade Wilson, subjected to an experiment to heal himself of cancer, obtains healing powers, but at the cost of becoming awfully disfigured. He then adopts the alter ego of Deadpool.", 'http://www.gstatic.com/tv/thumb/v22vodart/11098044/p11098044_v_v8_af.jpg', 'https://www.youtube.com/watch?v=9vN6DHB6bJc')

    dark_knight = media.Movie('The Dark Knight', "With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Harvey Dent (Aaron Eckhart), Batman (Christian Bale) has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.", 'http://www.gstatic.com/tv/thumb/v22vodart/173378/p173378_v_v8_at.jpg', 'https://www.youtube.com/watch?v=EXeTwQWrcwY')

    avengers_infinity_war = media.Movie('Avengers: Infinity War', "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.", 'http://www.gstatic.com/tv/thumb/v22vodart/12863030/p12863030_v_v8_ae.jpg', 'https://www.youtube.com/watch?v=6ZfuNTqbHE8')

    friends = media.Series('Friends', "Follow the lives of six reckless adults living in Manhattan, as they indulge in adventures which make their lives both troublesome and happening.", "https://peopledotcom.files.wordpress.com/2016/08/friends-435-5.jpg", "https://www.youtube.com/watch?v=XzaGBihfREw")

    that_70s_show = media.Series("That '70s Show", "Eric, a high school student, and his group of teenage friends struggle to lead purposeful lives whilst going through the tumultuous phase of adolescence.", "https://images-na.ssl-images-amazon.com/images/I/51CR295PR1L._SY445_.jpg", "https://www.youtube.com/watch?v=WiyfT_w4GwQ")
    how_i_met_your_mother = media.Series("How I Met Your Mother", "Ted Mosby, an architect, recounts to his children the events that led him to meet their mother. His journey is made more eventful by the presence of his friends Lily, Marshall, Robin and Barney.", "http://www.gstatic.com/tv/thumb/tvbanners/9916255/p9916255_b_v8_aa.jpg", "https://www.youtube.com/watch?v=o96UB-B-0C4")

    deathnote = media.Anime("Death Note", "Death Note is a Japanese manga series written by Tsugumi Ohba and illustrated by Takeshi Obata. The story follows Light Yagami, a high school student who stumbles across a mysterious otherworldly notebook: the 'Death Note', which belonged to the Shinigami Ryuk, and grants its user the power to kill anyone whose name and face he knows. The series centers around Light's subsequent attempts to use the Death Note to change the world into a utopian society without crime as a god-like vigilante named 'Kira' and the subsequent efforts of an elite task-force of law enforcement officials, consisting of members of the Japanese police agency led by L, an enigmatic international detective, to apprehend him and end his reign of terror.", "https://images-na.ssl-images-amazon.com/images/I/51c7O54CdkL.jpg", "https://www.youtube.com/watch?v=tJZtOrm-WPk")
    naruto = media.Anime("Naruto", "Naruto is a Japanese manga series written and illustrated by Masashi Kishimoto. It tells the story of Naruto Uzumaki, an adolescent ninja who searches for recognition from his peers and the village and also dreams of becoming the Hokage, the leader of his village.", "https://i.pinimg.com/originals/d0/b8/d8/d0b8d8d5f5309a0c9ecc1b9454fbed31.jpg", "https://www.youtube.com/watch?v=j2hiC9BmJlQ")
    full_metal = media.Anime("Fullmetal Alchemist: Brotherhood", "Brothers Edward and Alphonse Elric search for the Philsopher's Stone, hoping to restore their bodies, which were lost when they attempted to use their alchemy skills to resurrect their deceased mother. Edward, who lost only limbs, joins the State Military, which gives him the freedom to continue the search as he tries to restore his brother, whose soul is tethered to earth by a suit of armor. However, Edward and Alphonse are not the only ones seeking the powerful stone. And as they search, they learn of a plot to transmute the entire country for reasons they cannot comprehend.", "https://m.media-amazon.com/images/M/MV5BZmEzN2YzOTItMDI5MS00MGU4LWI1NWQtOTg5ZThhNGQwYTEzXkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_.jpg", "https://www.youtube.com/watch?v=BOm_PAI2goo")
    hunter_x_hunter = media.Anime("Hunter × Hunter", "The story focuses on a young boy named Gon Freecss, who discovers that his father, who he was told was dead, is actually alive and a world-renowned Hunter, a licensed profession for those who specialize in fantastic pursuits such as locating rare or unidentified animal species, treasure hunting, surveying unexplored enclaves, or hunting down lawless individuals. Despite being abandoned by his father, Gon departs upon a journey to follow in his footsteps, pass the rigorous Hunter Examination, and eventually find his father. Along the way, Gon meets various other Hunters and also encounters the paranormal.", "https://ae01.alicdn.com/kf/HTB1SMqNvAKWBuNjy1zjq6AOypXan/Hunter-x-Hunter-Poster-GI-Gon-Killua-Anime-Silk-Wall-Decor-Posters-24x34inch.jpg_640x640.jpg", "https://www.youtube.com/watch?v=d6kBeJjTGnY")
    attack_on_titan = media.Anime("Attack on Titan", "The story of Attack on Titan revolves around the adventures of Eren Jeager who lives in the town of Shinganshina. When Wall Maria is breached by the Colossal Titan, with the Armored Titan further compromising the town, chaos ensues as the Titans enters Shinganshina causing a mass evacuation. Eren vows to kill all the Titans after watching in horror as a smiling Titan eats his mother, Carla, his father having mysteriously disappeared after giving him a key to their basement. He then enlists in the military with his friends following suit.", "http://img1.ak.crunchyroll.com/i/spire3/962b75cb9f4905f2fd9dfa543610955e1416664140_full.jpg", "https://www.youtube.com/watch?v=MGRm4IzK1SQ")

    dark_knight.add_comment('Best scenes: https://www.youtube.com/watch?v=dMribC2uAdQ')
    avengers_infinity_war.add_comment('Loved when thor comes to earth')
    friends.add_comment('Watch season 2,3 and 4!! Great seasons')
    friends.add_comment('Joey punches ross : Episode: Season 9 Episode 2')
    friends.add_comment('Ross gets tan: S10E03')
    that_70s_show.add_comment('Enjoyed the circle..')
    that_70s_show.add_comment('Search for best circles on youtube..Had a lot of fun!!!')
    how_i_met_your_mother.add_comment('Jinx!!!! Enough to explain!')
    how_i_met_your_mother.add_comment("Barney's best moments search on Youtube")
    how_i_met_your_mother.add_comment("Last season was disappointing")
    deathnote.add_comment('Loved L!!!.. Bad move killing him..')
    naruto.add_comment('Sasuke vs Itachi')
    naruto.add_comment('Naruto vs Pain')
    naruto.add_comment('Naruto vs Sasuke End Fight')
    full_metal.add_comment('Death of lust')
    hunter_x_hunter.add_comment('Gon vs Pitou')
    attack_on_titan.add_comment('Eren vs female titan end fight')
    attack_on_titan.add_comment('Levi vs female titan')
    attack_on_titan.add_comment('Eren awakens The Coordinate')

    movies = [pulp_fiction, deadpool, dark_knight, avengers_infinity_war]
    series = [friends, that_70s_show, how_i_met_your_mother]
    anime = [deathnote, naruto, full_metal, hunter_x_hunter, attack_on_titan]

    return_seeded_list = []
    if allowed_movies:
        return_seeded_list += movies
    if allowed_series:
        return_seeded_list += series
    if allowed_anime:
        return_seeded_list += anime
    return return_seeded_list


def clear():
    '''
    Function that clears the screen
    Args: None
    Returns: Nothing
    '''
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
    # return


def print_input_filters(phase, videos=None):
    clear()
    clear()
    clear()
    curr_video_type = None

    if phase == PHASE_UPD_MOVIES or phase == PHASE_ADD_MOVIE:
        curr_video_type = 'Movie'
    elif phase == PHASE_UPD_SERIES or phase == PHASE_ADD_SERIES:
        curr_video_type = 'Series'
    elif phase == PHASE_UPD_ANIME or phase == PHASE_ADD_ANIME:
        curr_video_type = 'Anime'

    print(('Phase: ' + phase).center(disp_size, ':'))
    print('*' * disp_size)
    print(('Use seeded videos:' + str(seeded_videos_allowed)).center(disp_size, ' '))
    print(('Use seeded movies: ' + str(seeded_movies_allowed)).center(disp_size, ' '))
    print(('Use seeded series: ' + str(seeded_series_allowed)).center(disp_size, ' '))
    print(('Use seeded animes: ' + str(seeded_animes_allowed)).center(disp_size, ' '))
    if phase == PHASE_ADD_MOVIE and add_num_videos is not None:
        print(('Movies to add:' + str(add_num_videos)).center(disp_size, ' '))
        if curr_add_at is not None:
            print(('Adding movie at:' + str(add_num_videos - curr_add_at + 1)).center(disp_size, ' '))
    elif phase == PHASE_ADD_SERIES and add_num_videos is not None:
        print(('Series to add:' + str(add_num_videos)).center(disp_size, ' '))
        if curr_add_at is not None:
            print(('Adding series at:' + str(add_num_videos - curr_add_at + 1)).center(disp_size, ' '))
    elif phase == PHASE_ADD_ANIME and add_num_videos is not None:

        print(('Animes to add:' + str(add_num_videos)).center(disp_size, ' '))
        if curr_add_at is not None:
            print(('Adding anime at:' + str(add_num_videos - curr_add_at + 1)).center(disp_size, ' '))
    if videos is not None:
        str_title = curr_video_type + ' title:' + videos.title
        print(str_title.center(disp_size, ' '))
    print('*' * disp_size)
    print('\n\n')


def remove_duplicate_values(duplicate_list):
    return list(set(duplicate_list))


def input_seeded_or_not():
    global seeded_videos_allowed, seeded_animes_allowed, seeded_movies_allowed, seeded_series_allowed
    tmp_mov, tmp_ser, tmp_ani = [], [], []
    seeded_vids = seeded_videos()
    for video in seeded_vids:
        if video.type == 'M':
            tmp_mov.append(video)
        elif video.type == 'S':
            tmp_ser.append(video)
        elif video.type == 'A':
            tmp_ani.append(video)
        else:
            print('ERROR: Incorrect object type initialization')
    mov_str = '\n\t'.join([str(i + 1) + '. ' + movie.title for i, movie in enumerate(tmp_mov)])
    ser_str = '\n\t'.join([str(i + 1) + '. ' + series.title for i, series in enumerate(tmp_ser)])
    anime_str = '\n\t'.join([str(i + 1) + '. ' + anime.title for i, anime in enumerate(tmp_ani)])
    inp = ''
    while(1):
        print('Here are the seeded videos:')
        print('\nMovies:')
        print('\t' + mov_str)
        print('\nSeries:')
        print('\t' + ser_str)
        print('\nAnimes:')
        print('\t' + anime_str)
        print('\n\n')
        print('Want to add seeded videos to the website?\nPress :\n1. For adding seeded movies\n2. For adding seeded series\n3. For adding seeded animes')
        print('PS: You can add comma separated values without space separator')
        inp = input('Press Enter to exclude seeded videos or else choose from above!\nYour choice')
        is_valid_input = True
        if(inp == ''):
            seeded_videos_allowed = False
        else:
            seeded_videos_allowed = True
            split_comma_inp = inp.split(',')
            while(1):
                try:
                    split_comma_inp = list(map(int, split_comma_inp))
                    break
                except:
                    show_error(INV_INPUT, PHASE_SEEDED_DECIDE)
                    continue
            for i in split_comma_inp:
                if i not in range(1, 4):
                    is_valid_input = False
                    show_error(INV_INPUT, PHASE_SEEDED_DECIDE)
        if is_valid_input:
            break
    inp = remove_duplicate_values(list(map(int, inp.split(','))))
    for i in inp:
        if i == 1:
            seeded_movies_allowed = True
        elif i == 2:
            seeded_series_allowed = True
        elif i == 3:
            seeded_animes_allowed = True


def validate_before_commit(videos, video_type):
    print_input_filters(PHASE_VALIDATION)
    print('Here are the {video_type} you entered:'.format(video_type=video_type))
    for video in videos:
        video.print_formatted_output()
    choice = input('\n\nPlease double check all the information provided!\nPress Enter to accept! Any other key + Enter to modify:')
    if choice == '':
        return True
    else:
        return False


def print_formatted_title(videos):
    video_str_arr = [str(i + 1) + '. ' + video.title for i, video in enumerate(videos)]
    video_str = '\n'.join(video_str_arr)
    print(video_str)


def show_error(code, phase=None, videos=None):
    if phase is not None:
        print_input_filters(phase, videos)
    if code == INV_INPUT:
        print('Error'.center(disp_size, '+'))
        print('It appears you have entered incorrect data!'.center(disp_size, ' '))
        print('Please enter the correct value!!'.center(disp_size, ' '))
        print('+' * disp_size)
    else:
        print(code)


def update_video_at(videos, index, video_type):
    log('Entering update_video_at')
    video = videos[index]
    if video_type == 'movies':
        phase = PHASE_UPD_MOVIES
    if video_type == 'series':
        phase = PHASE_UPD_SERIES
    if video_type == 'anime':
        phase = PHASE_UPD_ANIME
    print_input_filters(phase, video)
    video.print_formatted_attrs()
    while(1):
        try:
            attr_indices = input('Choose from the above attributes: ')
            attr_indices = list(map(int, attr_indices.split(',')))
            break
        except:
            show_error(INV_INPUT, phase, video)
    if video.validate_attr_list(attr_indices):
        video.update_video_attrs(video_type, attr_indices)
    else:
        print('Please enter a valid attr')
    videos[index] = video
    return videos


def update_list_of_videos(videos, video_type, single_mode=False):
    global curr_add_at, add_num_videos
    curr_add_at = None
    add_num_videos = None
    log('Entering update_list_of_videos')
    if video_type == 'movies':
        phase = PHASE_UPD_MOVIES
    if video_type == 'series':
        phase = PHASE_UPD_SERIES
    if video_type == 'anime':
        phase = PHASE_UPD_ANIME
    print_input_filters(phase)
    log(video_type)
    print('Here are the {video_type} you added:'.format(video_type=video_type))
    log('updating in batch mode')
    print_formatted_title(videos)
    while(1):
        try:
            choice = int(input('Choose a number:'))
            break
        except:
            show_error(INV_INPUT, phase)
    log('Choice' + str(choice))
    while(1):
        if choice in range(1, len(videos) + 1):
            videos = update_video_at(videos, choice - 1, video_type)
            break
        else:
            show_error(INV_INPUT, phase)
            print_formatted_title(videos)
            while(1):
                try:
                    choice = int(input('Choose a number:'))
                    break
                except:
                    show_error(INV_INPUT, phase)
    is_safe_to_commit = validate_before_commit(videos, video_type)
    if not is_safe_to_commit:
        return update_list_of_videos(videos, video_type)
    else:
        log('in upd_individual')
        log('here: ' + ' '.join([v.title for v in videos]))
        return videos


def input_videos(input_type, upd_mode=False, video_upd=None):
    global add_num_videos, curr_add_at
    current_input = 'NONE'
    current_input_obj = None
    if input_type == INPUT_MOVIE_DTLS:
        current_input = 'movies'
        current_input_obj = media.Movie()
    elif input_type == INPUT_SERIES_DTLS:
        current_input = 'series'
        current_input_obj = media.Series()
    elif input_type == INPUT_ANIME_DTLS:
        current_input = 'anime'
        current_input_obj = media.Anime()

    if not upd_mode:
        if input_type == INPUT_MOVIE_DTLS:
            phase = PHASE_ADD_MOVIE
        elif input_type == INPUT_SERIES_DTLS:
            phase = PHASE_ADD_SERIES
        elif input_type == INPUT_ANIME_DTLS:
            phase = PHASE_ADD_ANIME
        print_input_filters(phase)
        while(1):
            try:
                n = int(input('Please enter number of ' + current_input + ' that you want to add :'))
                break
            except:
                show_error(INV_INPUT, phase)

        user_defined_videos = []
        add_num_videos = n

        while(n > 0):
            curr_add_at = n
            if input_type == INPUT_MOVIE_DTLS:
                current_input = 'movies'
                current_input_obj = media.Movie()
                print_input_filters(PHASE_ADD_MOVIE)
            elif input_type == INPUT_SERIES_DTLS:
                current_input = 'series'
                current_input_obj = media.Series()
                print_input_filters(PHASE_ADD_SERIES)
            elif input_type == INPUT_ANIME_DTLS:
                current_input = 'anime'
                current_input_obj = media.Anime()
                print_input_filters(PHASE_ADD_ANIME)
            if current_input_obj is None:
                print('There is some error!! Object not initialised properly!')
            video = current_input_obj.input_attr_values(current_input)
            user_defined_videos.append(video)
            n -= 1
        is_safe_to_commit = validate_before_commit(user_defined_videos, current_input)
        for video in user_defined_videos:
            video.print_formatted_output()
        if not is_safe_to_commit:
            log('entering update')
            user_defined_videos = update_list_of_videos(user_defined_videos, current_input)
            log('here: ' + ' '.join([v.title for v in user_defined_videos]))
            log('exiting update')

        return user_defined_videos
    else:
        if video_upd is None:
            print('Incorrect object initialization')
            return
        update_list_of_videos(video_upd, current_input)


def log(message, wait=False):
    '''
    This method prints or waits till the input is entered only when testing the code
    '''
    if run_mode == 'test' and wait:
        input(message)
    elif run_mode == 'test':
        print(message)
    return


def initialize_undefined_vals(videos):
    for video in videos:
        video.initialize_undefined_vals()
    return


def categorise_videos(videos):
    tmp_mov, tmp_ser, tmp_ani = [], [], []
    for video in videos:
        if video.type == 'M':
            tmp_mov.append(video)
        elif video.type == 'S':
            tmp_ser.append(video)
        elif video.type == 'A':
            tmp_ani.append(video)
        else:
            print('Invalid video obj initialization')
    return tmp_mov, tmp_ser, tmp_ani


def add_comments_commit(comment, videos):
    params = comment.split(':')
    param_index = params[0]
    if len(params) < 2:
        return (False, videos)
    if len(params) > 2:
        param_val = ':'.join([params[i] for i in range(1, len(params))])
    else:
        param_val = params[1]
    try:
        param_index = int(param_index)
    except:
        return (False, videos)
    if param_index not in range(1, len(videos) + 1):
        return (False, videos)
    videos[param_index - 1].add_comment(param_val)
    return (True, videos)


def add_comments_interface_ui(videos):
    print_input_filters(PHASE_ADD_COMMENTS)
    print('Here are the videos you added:')
    print_formatted_title(videos)
    print('Instructions to enter comments:')
    print('<Number>:<Comment>')
    print('Eg: 1:Comment 1')
    print('You can enter multiple comments for one video')
    print('Enter q to exit input')
    inp = ''
    while(inp != 'q'):
        while(1):
            inp = input('Enter comments:')
            if inp == 'q':
                break
            return_bool, videos = add_comments_commit(inp, videos)
            if (return_bool):
                break
            else:
                show_error(INV_INPUT, PHASE_ADD_COMMENTS)
                print('Here are the videos you added:')
                print_formatted_title(videos)
                print('Instructions to enter comments:')
                print('<Number>:<Comment>')
                print('Eg: 1:Comment 1')
                print('You can enter multiple comments for one video')
                print('Enter q to exit input')
    return videos


if __name__ == '__main__':
    clear()
    clear()
    clear()
    run_mode = 'main'
    if len(sys.argv) == 2:
        if sys.argv[1] == 'test':
            run_mode = sys.argv[1]
    input_type_choice_list = ['Movie', 'Series', 'Anime']
    input_seeded_or_not()
    print_input_filters(PHASE_SEEDED_DECIDE)
    videos = []
    if seeded_videos_allowed:
        log('Adding seeded videos.!')
        videos = seeded_videos(seeded_movies_allowed, seeded_series_allowed, seeded_animes_allowed)

    while(1):
        print('Please choose which types you want to add!')
        print('\n'.join([str(i + 1) + '. ' + temp for i, temp in enumerate(input_type_choice_list)]))
        print('Enter either individual number choice or comma separated value without space')
        print('Press enter to not add any values')
        choice = input('Enter your choice:')
        if choice == '':
            break
        split_comma_inp = choice.split(',')
        try:
            split_comma_inp = list(map(int, split_comma_inp))
        except:
            show_error(INV_INPUT, PHASE_SEEDED_DECIDE)
            continue
        for i in split_comma_inp:
            if i not in range(1, len(input_type_choice_list) + 1):
                show_error(INV_INPUT, PHASE_SEEDED_DECIDE)
                continue
        split_comma_inp = remove_duplicate_values(split_comma_inp)
        for i in split_comma_inp:
            if i == INPUT_MOVIE_DTLS + 1:
                print_input_filters(PHASE_ADD_MOVIE)
                videos += input_videos(INPUT_MOVIE_DTLS)
            elif i == INPUT_SERIES_DTLS + 1:
                print_input_filters(PHASE_ADD_SERIES)
                videos += input_videos(INPUT_SERIES_DTLS)
            elif i == INPUT_ANIME_DTLS + 1:
                print_input_filters(PHASE_ADD_ANIME)
                videos += input_videos(INPUT_ANIME_DTLS)
        break

    initialize_undefined_vals(videos)
    videos = add_comments_interface_ui(videos)
    for video in videos:
        video.escape_chars()
    movies, series, animes = categorise_videos(videos)
    fresh_tomatoes.open_page(movies, series, animes)
