# create-top-spotify-playlist
Create a 100-song playlist based on your top 10 artists.

1. Install Python 3.10
2. Create virtual environment -> python -m venv ./.venv
3. Activate the virtual environment -> ./.venv/scripts/activate
4. Install pip -> python -m pip install --upgrade pip
5. Install requirements -> pip install -r requirements.txt
6. Login at https://developer.spotify.com/dashboard/login
7. Create an app from your dashboard\
![Step 7](/pictures/step-7.png?raw=true)
8. Set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET variables in the run.py file with the Client ID and Client Secret from your app\
![Step 8](/pictures/step-8.png?raw=true)
9. Click "Edit settings" on your app's dashboard and add the redirect URI -> 'http://localhost:8888/callback' (make sure to click add and save!)\
![Step 9](/pictures/step-9.png?raw=true)
10. Run 'run.py'
