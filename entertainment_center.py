import media
import fresh_tomatoes
from video import Video


def seeded_videos():
    pulp_fiction = media.Movie('Pulp Fiction', "In the realm of underworld, a series of incidents intertwines the lives of two Los Angeles mobsters, a gangster's wife, a boxer and two small-time criminals.", 'https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg', "https://www.youtube.com/watch?v=tGpTpVyI_OQ")

    deadpool = media.Movie('Deadpool', "Mercenary Wade Wilson, subjected to an experiment to heal himself of cancer, obtains healing powers, but at the cost of becoming awfully disfigured. He then adopts the alter ego of Deadpool.", 'http://www.gstatic.com/tv/thumb/v22vodart/11098044/p11098044_v_v8_af.jpg', 'https://www.youtube.com/watch?v=9vN6DHB6bJc')

    dark_knight = media.Movie('The Dark Knight', "With the help of allies Lt. Jim Gordon (Gary Oldman) and DA Harvey Dent (Aaron Eckhart), Batman (Christian Bale) has been able to keep a tight lid on crime in Gotham City. But when a vile young criminal calling himself the Joker (Heath Ledger) suddenly throws the town into chaos, the caped Crusader begins to tread a fine line between heroism and vigilantism.", 'http://www.gstatic.com/tv/thumb/v22vodart/173378/p173378_v_v8_at.jpg', 'https://www.youtube.com/watch?v=EXeTwQWrcwY')

    avengers_infinity_war = media.Movie('Avengers: Infinity War', "Iron Man, Thor, the Hulk and the rest of the Avengers unite to battle their most powerful enemy yet -- the evil Thanos. On a mission to collect all six Infinity Stones, Thanos plans to use the artifacts to inflict his twisted will on reality. The fate of the planet and existence itself has never been more uncertain as everything the Avengers have fought for has led up to this moment.", 'http://www.gstatic.com/tv/thumb/v22vodart/12863030/p12863030_v_v8_ae.jpg', 'https://www.youtube.com/watch?v=6ZfuNTqbHE8')

    friends = media.Series('Friends', "Follow the lives of six reckless adults living in Manhattan, as they indulge in adventures which make their lives both troublesome and happening.", "https://peopledotcom.files.wordpress.com/2016/08/friends-435-5.jpg", "https://www.youtube.com/watch?v=XzaGBihfREw")

    that_70s_show = media.Series("That '70s Show", "Eric, a high school student, and his group of teenage friends struggle to lead purposeful lives whilst going through the tumultuous phase of adolescence.", "https://images-na.ssl-images-amazon.com/images/I/51CR295PR1L._SY445_.jpg", "https://www.youtube.com/watch?v=WiyfT_w4GwQ")
    how_i_met_your_mother = media.Series("How I Met Your Mother", "Ted Mosby, an architect, recounts to his children the events that led him to meet their mother. His journey is made more eventful by the presence of his friends Lily, Marshall, Robin and Barney.", "http://www.gstatic.com/tv/thumb/tvbanners/9916255/p9916255_b_v8_aa.jpg", "https://www.youtube.com/watch?v=o96UB-B-0C4")

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

    movies = [pulp_fiction, deadpool, dark_knight, avengers_infinity_war]
    series = [friends, that_70s_show, how_i_met_your_mother]
    print(friends.storyline)
    return movies, series


# v = Video('abc', 'def', 1)
# print(v.get_duration())
movies, series = seeded_videos()
fresh_tomatoes.open_page(movies, series)
