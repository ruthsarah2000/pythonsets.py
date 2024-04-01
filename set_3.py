'''
Task 1: Artist Lineup Compilation
You are provided with a list of artist names scheduled to perform at different stages of the music festival. Using a loop, compile these 
artist names into a set to create a unique lineup without duplicates.
'''

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()


for artist in artist_names:
    unique_artists.add(artist)

print("Unique lineup of artists:", unique_artists)

'''
You have a list of genres associated with each artist. Using a loop with sets, categorize artists by their genres, creating a set for each genre.
'''
artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock"
}
genre_sets = {}


for artist, genre in artists_genres.items():
    if genre in genre_sets:
        genre_sets[genre].add(artist)
    else:
        genre_sets[genre] = {artist}

for genre, artists in genre_sets.items():
    print(f"Artists in {genre}: {artists}")

'''
Task 3: Playlist Duplication Check
Create a Python script that takes multiple playlist sets and checks if any playlist is a duplicate of another (i.e., contains the same set of songs).
'''
playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]

playlist_sets = {}


for i, playlist in enumerate(playlists, start=1):
    playlist_set = frozenset(playlist)
    if playlist_set in playlist_sets.values():
        print(f"Playlist {i} is a duplicate of another playlist.")
        duplicate_index = list(playlist_sets.values()).index(playlist_set)
        print(f"It is a duplicate of Playlist {duplicate_index + 1}.")
    else:
        playlist_sets[i] = playlist_set

if len(playlist_sets) == len(playlists):
    print("No duplicate playlists found.")
    
