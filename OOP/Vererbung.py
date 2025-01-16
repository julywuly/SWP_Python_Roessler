class Artist:
    def __init__(self, name):
        if not isinstance(name, str):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Artist name must be a string.")
        self.name = name
        self.albums = []

    def add_album(self, album):
        if not isinstance(album, Album):  # Fehlerbehebung: Typüberprüfung
            raise TypeError("Only Album objects can be added.")
        self.albums.append(album)

    def __str__(self):
        return f"Artist: {self.name}, Albums: {[album.title for album in self.albums]}"


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
    album1.add_song(Song("Sculptures of anything goes", 5.2))

    album2 = Album("Humbug", 2023)
    album2.add_song(Song("Pretty Visitors", 3.8))
    album2.add_song(Song("My Propeller", 4.1))

    artist.add_album(album1)
    artist.add_album(album2)

    print(artist)
    for album in artist.albums:
        print(album)
except (TypeError, ValueError) as e:
    print(f"Error: {e}")
