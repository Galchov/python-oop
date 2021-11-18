from project.song import Song


class Album:
    def __init__(self, name, *args):
        self.name = name
        self.published = False
        self.songs = list(args)

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song in self.songs:
            return "Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        for el in self.songs:
            if el.name == song_name:
                self.songs.remove(el)
                return f"Removed song {song_name} from album {self.name}."
        return "Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        album_info = [f"Album {self.name}"]
        for song in self.songs:
            album_info.append(f"== {song.get_info()}")
        return "\n".join(album_info)
