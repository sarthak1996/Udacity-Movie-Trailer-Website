import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Entertainment Center!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .series-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .series-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
        @import url(http://fonts.googleapis.com/css?family=Roboto+Condensed:400,700);
        /* written by riliwan balogun http://www.facebook.com/riliwan.rabo*/
        .board{
        margin: 60px auto;
        background: #fff;
        /*box-shadow: 10px 10px #ccc,-10px 20px #ddd;*/
        }
        .board .nav-tabs {
            position: relative;
            /* border-bottom: 0; */
            /* width: 80%; */
            margin: 40px auto;
            margin-bottom: 0;
            box-sizing: border-box;

        }

        .board > div.board-inner{
            background: #fafafa url(http://subtlepatterns.com/patterns/geometry2.png);

        }

        p.narrow{
            width: 60%;
            margin: 10px auto;
        }

        .liner{
            height: 2px;
            background: #ddd;
            position: absolute;
            width: 80%;
            margin: 0 auto;
            left: 0;
            right: 0;
            top: 50%;
            z-index: 1;
        }

        .nav-tabs > li.active > a, .nav-tabs > li.active > a:hover, .nav-tabs > li.active > a:focus {
            color: #555555;
            cursor: default;
            /* background-color: #ffffff; */
            border: 0;
            border-bottom-color: transparent;
        }

        span.round-tabs{
            width: 70px;
            height: 70px;
            line-height: 70px;
            display: inline-block;
            border-radius: 100px;
            background: white;
            z-index: 2;
            position: absolute;
            left: 0;
            text-align: center;
            font-size: 25px;
        }

        span.round-tabs.one{
            color: rgb(34, 194, 34);border: 2px solid rgb(34, 194, 34);
        }

        li.active span.round-tabs.one{
            background: #fff !important;
            border: 2px solid #ddd;
            color: rgb(34, 194, 34);
        }

        span.round-tabs.two{
            color: #febe29;border: 2px solid #febe29;
        }

        li.active span.round-tabs.two{
            background: #fff !important;
            border: 2px solid #ddd;
            color: #febe29;
        }

        span.round-tabs.three{
            color: #3e5e9a;border: 2px solid #3e5e9a;
        }

        li.active span.round-tabs.three{
            background: #fff !important;
            border: 2px solid #ddd;
            color: #3e5e9a;
        }

        span.round-tabs.four{
            color: #f1685e;border: 2px solid #f1685e;
        }

        li.active span.round-tabs.four{
            background: #fff !important;
            border: 2px solid #ddd;
            color: #f1685e;
        }

        span.round-tabs.five{
            color: #ef0090;border: 2px solid #ef0090;
        }

        li.active span.round-tabs.five{
            background: #fff !important;
            border: 2px solid #ddd;
            color: #ef0090;
        }

        .nav-tabs > li.active > a span.round-tabs{
            background: #fafafa;
        }
        .nav-tabs > li {
            width: 20%;
        }
        /*li.active:before {
            content: " ";
            position: absolute;
            left: 45%;
            opacity:0;
            margin: 0 auto;
            bottom: -2px;
            border: 10px solid transparent;
            border-bottom-color: #fff;
            z-index: 1;
            transition:0.2s ease-in-out;
        }*/
        .nav-tabs > li:after {
            content: " ";
            position: absolute;
            left: 45%;
           opacity:0;
            margin: 0 auto;
            bottom: 0px;
            border: 5px solid transparent;
            border-bottom-color: #ddd;
            transition:0.1s ease-in-out;

        }
        .nav-tabs > li.active:after {
            content: " ";
            position: absolute;
            left: 45%;
           opacity:1;
            margin: 0 auto;
            bottom: 0px;
            border: 10px solid transparent;
            border-bottom-color: #ddd;

        }
        .nav-tabs > li a{
           width: 70px;
           height: 70px;
           margin: 20px auto;
           border-radius: 100%;
           padding: 0;
        }

        .nav-tabs > li a:hover{
            background: transparent;
        }

        .tab-content{
        }
        .tab-pane{
           position: relative;
        padding-top: 50px;
        }
        .tab-content .head{
            font-family: 'Roboto Condensed', sans-serif;
            font-size: 25px;
            text-transform: uppercase;
            padding-bottom: 10px;
        }
        .btn-outline-rounded{
            padding: 10px 40px;
            margin: 20px 0;
            border: 2px solid transparent;
            border-radius: 25px;
        }

        .btn.green{
            background-color:#5cb85c;
            /*border: 2px solid #5cb85c;*/
            color: #ffffff;
        }



        @media(){

            .board {
        width: 90%;
        height:auto !important;
        }
            span.round-tabs {
                font-size:16px;
        width: 50px;
        height: 50px;
        line-height: 50px;
            }
            .tab-content .head{
                font-size:20px;
                }
            .nav-tabs > li a {
        width: 50px;
        height: 50px;
        line-height:50px;
        }

        .nav-tabs > li.active:after {
        content: " ";
        position: absolute;
        left: 35%;
        }

        .btn-outline-rounded {
            padding:12px 20px;
            }
        }
        .row.heading h2 {
            color: #fff;
            font-size: 52.52px;
            line-height: 95px;
            font-weight: 400;
            text-align: center;
            margin: 0 0 40px;
            padding-bottom: 20px;
            text-transform: uppercase;
        }
        ul{
          margin:0;
          padding:0;
          list-style:none;
        }
        .heading.heading-icon {
            display: block;
        }
        .padding-lg {
            display: block;
            padding-top: 60px;
            padding-bottom: 60px;
        }
        .practice-area.padding-lg {
            padding-bottom: 55px;
            padding-top: 55px;
        }
        .practice-area .inner{
             border:1px solid #999999;
             text-align:center;
             margin-bottom:28px;
             padding:40px 25px;
        }
        .our-webcoderskull .cnt-block:hover {
            box-shadow: 0px 0px 10px rgba(0,0,0,0.3);
            border: 0;
        }
        .practice-area .inner h3{
            color:#3c3c3c;
            font-size:24px;
            font-weight:500;
            font-family: 'Poppins', sans-serif;
            padding: 10px 0;
        }
        .practice-area .inner p{
            font-size:14px;
            line-height:22px;
            font-weight:400;
        }
        .practice-area .inner img{
            display:inline-block;
        }
        .our-webcoderskull .cnt-block{
           float:left;
           width:100%;
           background:#fff;
           padding:30px 20px;
           text-align:center;
           border:2px solid #d5d5d5;
           margin: 0 0 28px;
        }
        .our-webcoderskull .cnt-block figure{
           width:148px;
           height:148px;
           border-radius:100%;
           display:inline-block;
           margin-bottom: 15px;
        }
        .our-webcoderskull .cnt-block img{
           width:148px;
           height:148px;
           border-radius:100%;
        }
        .our-webcoderskull .cnt-block h3{
           color:#2a2a2a;
           font-size:20px;
           font-weight:500;
           padding:6px 0;
           text-transform:uppercase;
        }
        .our-webcoderskull .cnt-block h3 a{
          text-decoration:none;
            color:#2a2a2a;
        }
        .our-webcoderskull .cnt-block h3 a:hover{
            color:#337ab7;
        }
        .our-webcoderskull .cnt-block p{
           color:#2a2a2a;
           font-size:13px;
           line-height:20px;
           font-weight:400;
        }
        .our-webcoderskull .cnt-block .follow-us{
            margin:20px 0 0;
        }
        .our-webcoderskull .cnt-block .follow-us li{
            display:inline-block;
            width:auto;
            margin:0 5px;
        }
        .our-webcoderskull .cnt-block .follow-us li .fa{
           font-size:24px;
           color:#767676;
        }
        .our-webcoderskull .cnt-block .follow-us li .fa:hover{
           color:#025a8e;
        }


    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });

        $(document).on('click', '.series-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.series-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });


        $(function(){
            $('a[title]').tooltip();
            });

    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->

    <section style="background:#efefe9;">
        <div class="container">
            <div class="row">
                <div class="board">
                    <div class="board-inner">
                        <ul class="nav nav-tabs" id="myTab">
                            <div class="liner"></div>
                            <li class="active">
                                <a href="#movies" data-toggle="tab" title="Movies">
                                  <span class="round-tabs one">
                                          <i class="glyphicon glyphicon-facetime-video"></i>
                                  </span>
                                </a>
                            </li>

                            <li>
                                <a href="#series" data-toggle="tab" title="Series">
                                    <span class="round-tabs two">
                                        <i class="glyphicon glyphicon-eye-open"></i>
                                    </span>
                                </a>
                            </li>

                            <li>
                                <a href="#comments" data-toggle="tab" title="Important comments">
                                     <span class="round-tabs three">
                                          <i class="glyphicon glyphicon-comment"></i>
                                     </span>
                                 </a>
                            </li>

                            <li>
                                <a href="#anime" data-toggle="tab" title="Add new">
                                    <span class="round-tabs four">
                                        <i class="glyphicon glyphicon-plus"></i>
                                    </span>
                                </a>
                            </li>
                            <li>
                                <a href="#about" data-toggle="tab" title="About">
                                    <span class="round-tabs five">
                                        <i class="glyphicon glyphicon-cog"></i>
                                    </span>
                                </a>
                            </li>

                        </ul>
                     </div>

                    <div class="tab-content">
                        <div class="tab-pane fade in active" id="movies">
                            {movie_tiles}
                        </div>
                        <div class="tab-pane fade" id="series">
                          {series_tiles}
                        </div>
                        <div class="tab-pane fade" id="comments">
                          {comments_tiles}
                        </div>
                        <div class="tab-pane fade" id="anime">
                          {add_new_tile}
                        </div>
                        <div class="tab-pane fade" id="about">
                          {add_new_tile}
                        </div>

                        <div class="clearfix"></div>
                    </div>

                </div>
            </div>
        </div>
    </section>

  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342" title="{movie_description}">
    <h2>{movie_title}</h2>
</div>
'''

series_tile_content = '''
<div class="col-md-6 col-lg-4 series-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342" title="{series_description}">
    <h2>{series_title}</h2>
</div>
'''

comments_tiles_header = '''
<section class="our-webcoderskull padding-lg">
  <div class="container">
    <ul class="row">
'''
comments_tile_content = '''
<li class="col-12 col-md-6 col-lg-3">
          <div class="cnt-block equal-hight" style="height: 349px;">
            <figure><img src="{poster_image}" class="img-responsive" alt=""></figure>
            <h3>{video_title}</h3>
            <p>{comment_text}</p>

          </div>
</li>
'''

comments_tiles_footer = '''
 </ul>
  </div>
</section>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_description=movie.storyline
        )
    return content


def create_series_tiles_content(series):
    content = ''
    for series_element in series:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', series_element.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', series_element.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += series_tile_content.format(
            series_title=series_element.title,
            poster_image_url=series_element.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            series_description=series_element.storyline
        )
    return content


def create_comment_tiles_content(videos):
    content = ''
    if videos is None:
        return "No comments yet!!"

    for video in videos:
        if video.has_comments():
            for comment in video.get_comments():
                content += comments_tile_content.format(
                    poster_image=video.poster_image_url,
                    video_title=video.title,
                    comment_text=comment)

    return comments_tiles_header + content + comments_tiles_footer


def open_page(movies=None, series=None):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content

    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies),
        series_tiles=create_series_tiles_content(series),
        comments_tiles=create_comment_tiles_content(series),
        add_new_tile='create_movie_tiles_content(movies)'
    )

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
