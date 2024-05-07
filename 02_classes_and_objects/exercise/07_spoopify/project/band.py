from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        for album_obj in self.albums:
            if album_obj.name == album.name:
                return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for album_obj in self.albums:
            if album_obj.name == album_name:
                if album_obj.published:
                    return "Album has been published. It cannot be removed."

                self.albums.remove(album_obj)
                return f"Album {album_obj.name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        print_info = [f"Band {self.name}"]
        for album_obj in self.albums:
            print_info.append(f"{album_obj.details()}")
        return "\n".join(print_info)


# Test code:
song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
