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

while True:
    print("Please choose your album (Invalid choice exits):")
    for index, album in enumerate(albums):
        print(index + 1, album[0])

    choice = int(input("Enter the number of your choice: "))
    print(choice)
    if choice < 1 or choice > (len(albums)):
        print("Invalid choice. Exiting...")
        break
