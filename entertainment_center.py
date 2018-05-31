import media
import fresh_tomatoes

# the following are the instances created of the Movie class

the_incredible_hulk = media.Movie("The Incredible Hulk",
   "https://upload.wikimedia.org/wikipedia/en/8/88/The_Incredible_Hulk_poster.jpg",  # NOQA
   "https://www.youtube.com/watch?v=xbqNb2PFKKA")

iron_man2 = media.Movie("Iron Man 2",
    "https://upload.wikimedia.org/wikipedia/en/e/ed/Iron_Man_2_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=6ziBFh3V1aM")

thor = media.Movie("Thor",
    "https://upload.wikimedia.org/wikipedia/en/f/fc/Thor_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=JOddp-nlNvQ")

captain_america_the_first_avenger = media.Movie("Captain America",
    "https://upload.wikimedia.org/wikipedia/en/3/37/Captain_America_The_First_Avenger_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=JerVrbLldXw")

the_avengers = media.Movie("The Avengers",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=1yKqLNnxGZw")

iron_man3 = media.Movie("Iron Man 3",
    "https://upload.wikimedia.org/wikipedia/en/d/d5/Iron_Man_3_theatrical_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

thor_the_dark_world = media.Movie("Thor: The Dark World",
    "https://upload.wikimedia.org/wikipedia/en/7/7e/Thor_-_The_Dark_World_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=npvJ9FTgZbM")

captain_america_the_winter_soldier = media.Movie("Captain America 2",
    "https://upload.wikimedia.org/wikipedia/en/e/e8/Captain_America_The_Winter_Soldier.jpg",  # NOQA
    "https://www.youtube.com/watch?v=tbayiPxkUMM")

avengers_age_of_ultron = media.Movie("Avengers: Age of Ultron",
    "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko",  # NOQA
    "https://www.youtube.com/watch?v=FAfR8omt-CY")

captain_america_civil_war = media.Movie("Captain America: Civil War",
    "https://upload.wikimedia.org/wikipedia/en/5/53/Captain_America_Civil_War_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=dKrVegVI0Us")

spider_man_homecoming = media.Movie("Spider-Man: Homecoming",
    "https://upload.wikimedia.org/wikipedia/en/f/f9/Spider-Man_Homecoming_poster.jpg",  # NOQA
    "https://www.youtube.com/watch?v=n9DwoQ7HWvI")

# all instances are grouped together in a list
movies = [the_incredible_hulk, iron_man2, thor,
          captain_america_the_first_avenger,
          the_avengers, iron_man3, thor_the_dark_world,
          captain_america_the_winter_soldier,
          avengers_age_of_ultron, captain_america_civil_war,
          spider_man_homecoming]

# movies list sent to function in fresh_tomatoes to open movies page
fresh_tomatoes.open_movies_page(movies)
