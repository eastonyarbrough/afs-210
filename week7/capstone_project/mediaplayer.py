import random

class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
class Playlist:
    def __init__(self):
        self.songs = []

    def isEmpty(self):
        return self.songs == []

    def enqueue(self, song):
        self.songs.insert(0, song)

    def dequeue(self):
        return self.songs.pop()

    def requeue(self):
        song = self.songs[0]
        self.songs.insert(len(self.songs), song)
        self.songs.pop(0)

    def peek(self):
        return self.songs[len(self.songs)-1]

    def size(self):
        return len(self.songs)

    def clear(self):
        self.songs.clear()

    def showList(self):
        for song in self.songs:
            print(f'{song.title} by {song.artist}')

current_playlist = Playlist()

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        song_title = input('Please enter song title: ')
        art_name = input('Please enter artist name: ')
        # Add song to playlist
        new_song = Song(song_title, art_name)
        current_playlist.enqueue(new_song)
        print(f"New Song Added to Playlist: {song_title} by {art_name}")
        # print(f'{current_playlist.songs[0].title}')

    elif choice == 2:
        # Prompt user for Song Title
        song_title = input('Please enter song title: ')
        # remove song from playlist
        count = 0
        def search(rmv_title, count):
            if count >= current_playlist.size():
                print(f'{song_title} was not found. Please try again.')
            elif rmv_title.lower() == current_playlist.peek().title.lower():
                removed = current_playlist.dequeue()
                print(f"{removed.title} by {removed.artist} Removed from Playlist")
            elif rmv_title.lower() != current_playlist.peek().title.lower():
                not_it = current_playlist.dequeue()
                current_playlist.enqueue(not_it)
                count += 1
                return search(rmv_title, count)
        search(song_title, count)

    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        if int(current_playlist.size()) > 0:
            print("Playing....")
            print(f'{current_playlist.peek().title} by {current_playlist.peek().artist}')
        else:
            print('No songs in playlist')

    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        if int(current_playlist.size()) > 0:
            skipped = current_playlist.dequeue()
            current_playlist.enqueue(skipped)
            print("Skipping....")
            print('Now Playing...')
            print(f'{current_playlist.peek().title} by {current_playlist.peek().artist}')
        else:
            print('No songs in playlist')

    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        if int(current_playlist.size()) > 0:
            current_playlist.requeue()
            print("Replaying....")
            print(f'{current_playlist.peek().title} by {current_playlist.peek().artist}')
        else:
            print('No songs in playlist')

    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        shuffled = []
        def shuffle(lst):
            temp = lst.copy()
            if len(temp) > 0:
                song = temp.pop(random.randint(0, len(temp)-1))
                shuffled.append(song)
                return shuffle(temp)
            else:
                current_playlist.clear()
                for song in shuffled:
                    current_playlist.enqueue(song)         
        # Display song name that is now playing
        if int(current_playlist.size()) > 0:      
            shuffle(current_playlist.songs)
            print("Shuffling....")  
            print('Now Playing...')
            print(f'{current_playlist.peek().title} by {current_playlist.peek().artist}')
        else:
            print('No songs in playlist')

    elif choice == 7:
        # Display the song name and artist of the currently playing song
        if int(current_playlist.size()) > 0:
            print("Currently playing: ", end=" ")
            print(f'{current_playlist.peek().title} by {current_playlist.peek().artist}')
        else:
            print('No songs in playlist')

    elif choice == 8:
        # Show the current song list order
        if int(current_playlist.size()) > 0:
            print("\nSong list:\n")
            current_playlist.showList()
        else:
            print('No songs in playlist')

    elif choice == 0:
        print("Goodbye.")
        break
