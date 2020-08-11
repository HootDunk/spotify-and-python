# spotify-and-python
A collection of programs which connect to the spotify API using the Spotipy library to solve some problems and add some features

"copy_library_to_playlist.py" copies all of the songs in the "Liked Songs" part
of your library into a designated playlist. Currently Spotify does not offer an option
to share your liked songs with someone, only playlists. So I made this 
script to get around that.

"find_missing_tracks.py" saves a record of your library which can be cross referenced with your current songs to find if any are missing.  The "Like" button is next to the pause button on Spotify and I found myself accidently deleting things, sometimes without realizing/remembering the song name. This was especiallty common on runs and it could be tedius to go back and re-save the song in that moment.  This way I can find which songs it happened to for when I go to re-save them at a later time.  

"sleep-timer-v1.py" allows you to play a designated number of songs before your PC is set to sleep.  I liked the sleep timer that is available for podcasts and wanted to have that option for music as well.  Planning on adding a pause or sleep option in case you simply want the playback to stop after a designated amount of songs.  May also add the option of doing it by time limit as well. 
