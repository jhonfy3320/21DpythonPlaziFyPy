from node import Node

class Playlist:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def addSong(self, song):
        new_node = Node(song)
        if not self.top:
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1

    def playSong(self):
        if not self.top:
            raise Exception("No hay canciones en la lista")
        song = self.top.value
        self.top = self.top.next
        self.length -= 1
        return song

    def getPlaylist(self):
        playlist = []
        current = self.top
        while current:
            playlist.append(current.value)
            current = current.next
        return playlist

# Ejemplo 1
playlist = Playlist()
playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")

print(playlist.playSong())  # Output: "Hotel California"
print(playlist.playSong())  # Output: "Stairway to Heaven"
print(playlist.playSong())  # Output: "Bohemian Rhapsody"
print(playlist.playSong())  # Output: Error: No hay canciones en la lista

# Ejemplo 2
playlist = Playlist()
playlist.addSong("Bohemian Rhapsody")
playlist.addSong("Stairway to Heaven")
playlist.addSong("Hotel California")

print(playlist.getPlaylist())  # Output: ["Hotel California", "Stairway to Heaven", "Bohemian Rhapsody"]
