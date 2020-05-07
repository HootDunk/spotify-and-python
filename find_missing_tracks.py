import sys
import pickle
import spotipy
import spotipy.util as util

USERNAME = 'hootmx198' #your spotify username
CLIENT_ID = '5e67baffd423477b81fb43abb8101b9a'#set at your developer account
CLIENT_SECRET = 'Enter you cleint client_secret here!' #set at your developer account
REDIRECT_URI = 'http://localhost:8000' #set at your developer account, usually "http://localhost:8000"
SCOPE = 'user-library-read'

token = util.prompt_for_user_token(username = USERNAME, 
                                   scope = SCOPE, 
                                   client_id = CLIENT_ID, 
                                   client_secret = CLIENT_SECRET, 
                                   redirect_uri = REDIRECT_URI)

if token:
  sp = spotipy.Spotify(auth=token)
  results = sp.current_user_saved_tracks(limit=50)
  tracks_data = results['items']

  while results['next']:
    results = sp.next(results)
    tracks_data.extend(results['items'])

  # making a nested list of the relevant info (song id, track name, artist name)
  # also making a list of just the ids to make parsing by song id easier
  current_track_info = []
  current_track_id = []
  for track_data in tracks_data:
    temp_list = []
    track_id = track_data['track']['id']
    artist_name = track_data['track']['artists'][0]['name']
    track_name = track_data['track']['name']

    temp_list.append(track_id)
    temp_list.append(artist_name)
    temp_list.append(track_name)

    current_track_info.append(temp_list)
    current_track_id.append(track_id)


  try:
    #loading old library records from file
    with open('past_track_info.data', 'rb') as filehandle:
      past_track_info = pickle.load(filehandle)
  except FileNotFoundError:
    #This gives the option to save a record if there wasn't one recorded
    if input("You do not have a record saved, would you like to save one now? y/n ") == 'y':
        with open('past_track_info.data', 'wb') as filehandle:
          pickle.dump(current_track_info, filehandle)
        print("Record Saved")

    sys.exit()


  if past_track_info == current_track_info:
    print('All songs are accounted for')
  else:
    print("The missing songs are:")
    for item in past_track_info:
      if item[0] not in current_track_id:
        print(f"-'{item[2]} by {item[1]}")
        print(f"\t Song ID: {item[0]}")
    print("Enter the song ID in the browser to find the song")


  if input('Would you like to update your playlist? y/n: ') == 'y':
    #writing the track info to a file
    with open('past_track_info.data', 'wb') as filehandle:
      pickle.dump(current_track_info, filehandle)

  else:
    print('goodbye :)')

else:
  print("Can't get token for", username)




# change the last if input.  if missing songs -> displayt them else -> ask to update records