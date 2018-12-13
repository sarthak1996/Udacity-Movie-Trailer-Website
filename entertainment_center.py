import media
import fresh_tomatoes
from video import Video

seeded_videos_allowed = True
movies = []
anime = []
series = []

'''
CONSTANTS START
'''
INV_INPUT = 'Invalid Input'

'''
CONSTANTS END
'''


def seeded_videos():
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

    return movies, series, anime


def input_seeded_or_not():
    global seeded_videos_allowed
    tmp_mov, tmp_ser, temp_ani = seeded_videos()
    mov_str = '\n'.join([(i + 1) + '. ' + movie for i, movie in enumerate(tmp_mov)])
    ser_str = '\n'.join([(i + 1) + '. ' + series for i, series in enumerate(tmp_ser)])
    anime_str = '\n'.join([(i + 1) + '. ' + anime for i, anime in enumerate(tmp_ani)])
    print('Here are the seeded videos:')
    print('Movies:')
    print(mov_str)
    print('Series:')
    print(ser_str)
    print('Animes:')
    print(anime_str)
    print('\n\n')
    inp = input('Want to add seeded videos to the website?\nPress Enter to include seeded videos! Any other key + Enter to exclude!')
    if(inp is None):
        seeded_videos_allowed = True
    else:
        seeded_videos_allowed = False


def validate_before_commit(videos, video_type):
    print('Here is the list of {video_type} you entered:'.format(video_type=video_type))
    for video in videos:
        video.print_formatted_output()
    choice = input('Please double check all the information provided!\nPress Enter to accept! Any other key + Enter to modify:')
    if choice is None:
        return True
    else:
        return False


def print_formatted_title(videos):
    video_str_arr = [(i + 1) + '. ' + video for i, video in enumerate(videos)]
    video_str = '\n'.join(video_str_arr)
    return video_str


def show_error(code):
    if code == INV_INPUT:
        print('It seems you have entered data incorrectly!!\nPlease enter again!')


def update_video_at(videos, index):
    video = videos[index]
    video.print_formatted_attrs()
    attr_indices = input('Choose from the above attributes: ')
    attr_indices = map(int, attr_indices.split(','))
    if video.validate_attr_list(attr_indices):
        video.input_attr_values()
    else:
        print('Please enter a valid attr')


def update_list_of_videos(videos, video_type):
    print('Here are the {video_type}s you added:')
    print_formatted_title(videos)
    choice = input('Choose a number:')
    while(1):
        if choice in range(1, len(videos) + 1):
            videos = update_video_at(videos, choice - 1)
        else:
            show_error(INV_INPUT)
            print_formatted_title(videos)
            choice = input('Choose a number:')
    is_safe_to_commit = validate_before_commit(videos)
    if not is_safe_to_commit:
        update_list_of_videos(videos, video_type)
    else:
        return videos


def input_movies():
    n = input('Please enter number of movies that you want to add :')
    user_defined_movies = []
    while(n > 0):
        movie = media.Movie()
        movie.title = input('Enter movie name :')
        movie.storyline = input('Enter movie description :')
        movie.poster_image_url = input('Enter movie poster url :')
        movie.trailer_youtube_url = input('Enter movie trailer :')
        user_defined_movies += movie
    is_safe_to_commit = validate_before_commit(user_defined_movies)
    if not is_safe_to_commit:
        user_defined_movies = update_list_of_videos(user_defined_movies)
    else:
        return user_defined_movies


fresh_tomatoes.open_page(movies, series, anime)
