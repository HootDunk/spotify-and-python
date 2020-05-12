import spotipy
import spotipy.util as util
import time
import os


USERNAME = 'hootmx198' #your spotify username
CLIENT_ID = '5e67baffd423477b81fb43abb8101b9a'#set at your developer account
CLIENT_SECRET = 'b3f1d01e33e14875bee10ea18e0ec8ae' #set at your developer account
REDIRECT_URI = 'http://localhost:8000' 
SCOPE = 'user-read-currently-playing'
# scope = 'user-read-playback-state'
# works as well

token = util.prompt_for_user_token(username= USERNAME, scope = SCOPE, client_id=CLIENT_ID
	, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

# get authentication token
spotify = spotipy.Spotify(auth=token)

# ask user for song limit
song_limit = int(input('How many songs would you like played before sleep? '))



# while loop to check song and count songs played based on song id
songs_played = []
while len(songs_played) <= song_limit:
	time.sleep(5)
	current_track_data = spotify.current_user_playing_track()
	song_id = current_track_data['item']['id']

	if song_id not in songs_played:
		songs_played.append(song_id)


# Puts PC to sleep
os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


# print(f'The song "{current_track_data["item"]["name"]}"'
# 	f' by {current_track_data["item"]["artists"][0]["name"]} has a popularity rating '
# 	f'of {current_track_data["item"]["popularity"]}.')




# could look in to using the duration_ms value as a way to set the sleep function. 
# This would reduce frequency of function calls