albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devel's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready For Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' on"),
         (8, "Seagull"),
     ]),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned To Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]),
    ("More Mayhem", "Emilda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]),
]

SONGS_LIST_INDEX = 3  # This is a Python convention of defining Constants. A constant mustn't be changed.
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (Invalid choice exits).")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index + 1, title))
    # for index, album in enumerate(albums):
    #     title, artist, year, songs = album
    #     print("{}: {} by {} released in {}".format(index + 1, title, artist, year, songs))
    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice - 1][SONGS_LIST_INDEX]
    else:
        continue

    print("Please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    song_choice = int(input())
    if 1 < song_choice <= len(songs_list):
        title = songs_list[song_choice - 1][SONG_TITLE_INDEX]
        print("Playing {}".format(title))

    print("=" * 40)
