# create-top-spotify-playlist
Create a 100-song playlist based on your top 10 artists.

1. Install Python 3.10
2. Create virtual environment -> python -m venv ./.venv
3. Install pip -> python -m pip install --upgrade pip
4. Install requirements -> pip install -r requirements.txt
5. Login at https://developer.spotify.com/dashboard/login
6. Create an app from your dashboard
![Step 6](/pictures/step-6.png?raw=true)
7. Set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET variables in the .env file with the Client ID and Client Secret from your app
![Step 7](/pictures/step-7.png?raw=true)
8. Click "Edit settings" on your app's dashboard and add the redirect URI -> 'http://localhost:8888/callback' (make sure to click add and save!)
![Step 8](/pictures/step-8.png?raw=true)
9. Run 'run.py'
