import sys
import spotipy
import spotipy.util as util

USERNAME = 'hootmx198' #your spotify username
CLIENT_ID = '5e67baffd423477b81fb43abb8101b9a'#set at your developer account
CLIENT_SECRET = 'put you secret credentials in this string' #set at your developer account
REDIRECT_URI = 'http://localhost:8000' #set at your developer account, usually "http://localhost:8000"
SCOPE = 'user-library-read'

token = util.prompt_for_user_token(username = USERNAME, 
                                   scope = SCOPE, 
                                   client_id = CLIENT_ID, 
                                   client_secret = CLIENT_SECRET, 
                                   redirect_uri = REDIRECT_URI)

# If token, we are getting all the track info under the key 'items'
if token:
  sp = spotipy.Spotify(auth=token)
  results = sp.current_user_saved_tracks(limit=50)
  tracks_data = results['items']

  while results['next']:
    results = sp.next(results)
    tracks_data.extend(results['items'])

# We want the track Id's so we are making a list of all the ids in a list called library ids
library_ids = []
for track_data in tracks_data:
    library_ids.append(track_data['track']['id'])
    #track_id = track_data['track']['id']
    #library_ids.append(track_id)


#moving songs from library_ids list into the designated playlist

#must modify scope to do so
token = util.prompt_for_user_token(username = USERNAME, 
                                   scope = 'playlist-modify-public', 
                                   client_id = CLIENT_ID, 
                                   client_secret = CLIENT_SECRET, 
                                   redirect_uri = REDIRECT_URI)

#parameter for which playlist to add to (can be found in the url of the playlist)
playlist_id = 'put your playlist id here'
#made a new list under a different name to make it a bit more readable.  Although it is a bit redundant. 
track_ids = library_ids

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False

#adding songs 100 at a time until there a fewer then 100. last few get added and the loops exits. 
    while len(track_ids) != 0:
      if len(track_ids) <= 100:
        sp.user_playlist_add_tracks(USERNAME, playlist_id, track_ids)
        track_ids.clear()
      elif len(track_ids) > 100:
        temp_track_ids = track_ids[0:100]
        sp.user_playlist_add_tracks(USERNAME, playlist_id, temp_track_ids)
        del track_ids[0:100]

else:
    print("Can't get token for", username)
