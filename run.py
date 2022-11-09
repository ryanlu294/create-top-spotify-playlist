import spotipy
from spotipy.oauth2 import SpotifyOAuth

def create_top_playlist(playlist_name, time_range):
    SPOTIPY_CLIENT_ID=''  # PUT YOUR CLIENT ID HERE
    SPOTIPY_CLIENT_SECRET='' # PUT YOUR CLIENT SECRET HERE
    SPOTIPY_REDIRECT_URI='http://localhost:8888/callback' # ADD THIS REDIRECT URI TO YOUR APP SETTINGS
    scope = ["user-top-read", "playlist-modify-public"]
    artist_list = []
    top_tracks = []
    playlist_id = 0

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri=SPOTIPY_REDIRECT_URI))

    results = sp.current_user_top_artists(limit=10, time_range=time_range)
    username = sp.current_user()['id']

    for item in results['items']:
        artist_list.append(item['id'])

    for artist in artist_list:
        top_ten_tracks = sp.artist_top_tracks(artist)
        for track in top_ten_tracks['tracks']:
            top_tracks.append(track['uri'])

    sp.user_playlist_create(user=username,name=playlist_name)

    playlists_object = sp.user_playlists(user=username)
    for i, playlist in enumerate(playlists_object['items']):
        if playlist['name'] == playlist_name:
            playlist_id = i
    playlist = playlists_object['items'][playlist_id]['uri']

    sp.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=top_tracks)

playlist_name = input('Enter playlist name: ')
user_time_range = input('short ~4 weeks, medium ~6 months, long ~several years \nEnter a timeframe: ')
time_range = {
    'short': 'short_term',
    'medium': 'medium_term',
    'long': 'long_term',
}

create_top_playlist(playlist_name, time_range[user_time_range])
