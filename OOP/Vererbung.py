class Artist:
    def __init__(self, name):
        if not isinstance(name, str):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Artist name must be a string.")
        self.name = name
        self.albums = []

    def add_album(self, alb):
        if not isinstance(alb, Album):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Only Album objects can be added.")
        # Neuer Fehler (behebbar): Album darf nicht doppelt hinzugefügt werden
        if alb in self.albums:
            print(f"Warning: Album '{alb.title}' already added. Skipping...")
            return
        self.albums.append(alb)

    def __str__(self):
        return f"Artist: {self.name}, Albums: {[albums.title for albums in self.albums]}"


class Album:
    def __init__(self, title, year):
        if not isinstance(title, str):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Album title must be a string.")
        if not isinstance(year, int):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Year must be an integer.")
        self.title = title
        self.year = year
        self.songs = []

    def add_song(self, song):
        if not isinstance(song, Song):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Only Song objects can be added.")
        # Hochblubber-Fehler (behebbar): Song-Titel doppelt
        try:
            if song.title in [s.title for s in self.songs]:
                raise ValueError(f"Duplicate song title: '{song.title}' already exists in the album.")
        except ValueError as err:
            print(f"Warning: {err}. Skipping...")
            return
        self.songs.append(song)

    def __str__(self):
        if not self.songs:  # Fehlerbehebung: Leere Liste behandeln
            return f"Album: {self.title} ({self.year})\n  No songs available."
        song_list = "\n  ".join(str(song) for song in self.songs)
        return f"Album: {self.title} ({self.year})\n  Songs:\n  {song_list}"


class Song:
    def __init__(self, title, duration):
        if not isinstance(title, str):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Song title must be a string.")
        if not isinstance(duration, (int, float)):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Duration must be a number.")
        if duration <= 0:  # Fehlerbehebung: Negative oder null Dauer verhindern
            raise ValueError("Duration must be a positive number.")
        self.title = title
        self.duration = duration  # in minutes

    def __str__(self):
        return f"{self.title} - {self.duration} min"


try:
    artist = Artist("Arctic Monkeys")

    album1 = Album("The Car", 2022)
    album1.add_song(Song("Mr. Schwartz", 3.5))
    album1.add_song(Song("The Car", 4.0))
    album1.add_song(Song("Mr. Schwartz", 3.5))  # Hochblubber-Fehler (behebbar)

    album2 = Album("Humbug", 2023)
    album2.add_song(Song("Pretty Visitors", 3.8))
    album2.add_song(Song("My Propeller", 4.1))

    artist.add_album(album1)
    artist.add_album(album1)  # Neuer Fehler (behebbar)
    artist.add_album(album2)

    # Neuer Fehler (NICHT behebar): ungültiger Album-Titel
    try:
        invalid_album = Album(123, 2024)
        artist.add_album(invalid_album)
    except TypeError as e:
        print(f"Critical Error: {e}. Cannot continue with invalid album.")

    # Hochblubber-Fehler (NICHT behebar): ungültige Song-Dauer
    try:
        album2.add_song(Song("Invalid Song", -2))
    except ValueError as e:
        print(f"Critical Error: {e}. Cannot add invalid song.")

    print(artist)
    for album in artist.albums:
        print(album)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
