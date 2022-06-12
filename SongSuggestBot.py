import os
import random
import discord
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Constants holding necessary id's and uri's
SPOTIFY_ID = ''
SPOTIFY_SECRET = ''
PLAYLIST_IDs = ['ENTER PLAYLIST URI\s']
AUTH_MANAGER = SpotifyClientCredentials(client_id=SPOTIFY_ID, client_secret=SPOTIFY_SECRET)
SP = spotipy.Spotify(auth_manager=AUTH_MANAGER)
CLIENT = discord.Client()

def get_tracks():
    tracks = []
    results = SP.playlist(random.choice(PLAYLIST_IDs))
        
    for item in results['tracks']['items']:
        tracks.append(item['track']['artists'][0]['name'] + ' - ' +
            item['track']['name'])
        
    return tracks

def get_random_track():
    tracks = get_tracks()
    song = random.choice(tracks)
    
    return song

# Used to register an event. 
@CLIENT.event
async def on_ready():
    CLIENT.user
 
@CLIENT.event
async def on_message(message):
    song = get_random_track()
    if message.author == CLIENT.user:
        return
    
    if message.content.startswith('!new song'):
        await message.channel.send(song)
        
CLIENT.run('[ENTER BOT TOKEN]')
