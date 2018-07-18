playlist = {"title": "Patagonia Bus",
 	"author": "Marius Toader",
 	"songs": [
 		{"title": "song1", "artist": ["blue"], "duration": 2.35},
 		{"title": "song2", "artist": ["kitty", "dj kat"], "duration": 2.55},
 		{"title": "miau", "artist": ["garfield"], "duration": 2.00}
	]
}

total_length = 0
for song in playlist["songs"]:
	total_length += song["duration"]

print(total_length)