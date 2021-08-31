# A Spotify playlist Application developed by Brian Hwang, 2021. 
# Copyright © 2021 Brian Hwang. All rights reserved.
import math
import spotipy
import re
from spotipy import SpotifyOAuth
def create_playlist (num_tracks, num_playlists, url_list, playlist_name):
    CLIENT_ID = ''
    CLIENT_SECRET = ''
    REDIRECT_URI = 'http://localhost:8888/callback'
    scope = 'playlist-modify-public'
    username = ''

    token = SpotifyOAuth(client_id=CLIENT_ID,client_secret=CLIENT_SECRET,redirect_uri=REDIRECT_URI,scope=scope,username=username)
    spotifyObject = spotipy.Spotify(auth_manager=token)
    playlist_ids = []
    num_playlists = int(num_playlists)
    num_tracks = int(num_tracks)
    for i in range(num_playlists):
        url = url_list[i]
        new_url = re.sub('https://open.spotify.com.*?playlist/', '', url)
        if '?' in new_url:
            split = new_url.split('?',1)
            new_url = split[0]
        playlist_ids.append(new_url)
    seeds = [] #this will be used as seeds to generate recommended playlist
    for id in playlist_ids: #for each playlist, get their tracks and put them into a list
        get_tracks = spotifyObject.playlist_tracks(playlist_id=id)
        tracks = []
        for i in range(len(get_tracks['items'])):
            track_id = get_tracks['items'][i]['track']['id']
            tracks.append(track_id)
        playlist_info = spotifyObject.audio_features(tracks=tracks) #gets audio features for each track in the playlist
        sum_acoustic = sum_dance = sum_energy = sum_instrumental = sum_liveness = sum_loudness = \
        sum_speech = sum_tempo = sum_valence = 0
        for i in range(len(playlist_info)): #go thru each song's traits
            sum_acoustic += playlist_info[i]['acousticness']
            sum_dance += playlist_info[i]['danceability']
            sum_energy += playlist_info[i]['energy']
            sum_instrumental += playlist_info[i]['instrumentalness']
            sum_liveness += playlist_info[i]['liveness']
            sum_loudness += playlist_info[i]['loudness']
            sum_speech += playlist_info[i]['speechiness']
            sum_tempo += playlist_info[i]['tempo']
            sum_valence += playlist_info[i]['valence']
        avg_acoustic = sum_acoustic/len(playlist_info)
        avg_dance = sum_dance/len(playlist_info)
        avg_energy = sum_energy/len(playlist_info)
        avg_instrumental = sum_instrumental/len(playlist_info)
        avg_liveness = sum_liveness/len(playlist_info)
        avg_loudness = sum_loudness/len(playlist_info)
        avg_speech = sum_speech/len(playlist_info)
        avg_tempo = sum_tempo/len(playlist_info)
        avg_valence = sum_valence/len(playlist_info)
        best_song_id = None
        best_distance = float('inf')
        for i in range(len(playlist_info)): #go thru each song again to find the best representative song
            calculated_distance = math.sqrt((playlist_info[i]['acousticness']-avg_acoustic)**2 + (playlist_info[i]['danceability']-avg_dance)**2 \
            + (playlist_info[i]['energy']-avg_energy)**2 + (playlist_info[i]['instrumentalness']-avg_instrumental)**2 + \
            (playlist_info[i]['liveness']-avg_liveness)**2 + (playlist_info[i]['loudness']-avg_loudness)**2 + \
            (playlist_info[i]['speechiness']-avg_speech)**2 + (playlist_info[i]['tempo']-avg_tempo)**2 + \
            (playlist_info[i]['valence']-avg_valence)**2)
            if calculated_distance < best_distance:
                best_distance = calculated_distance
                best_song_id = playlist_info[i]['id']
        seeds.append(best_song_id)
    recommendations = spotifyObject.recommendations(seed_tracks=seeds,limit=num_tracks)
    ids = []
    for i in range(num_tracks):
        ids.append(recommendations['tracks'][i]['id'])
    spotifyObject.user_playlist_create(user=username,name=playlist_name)
    preplaylist = spotifyObject.user_playlists(user=username)
    playlist = preplaylist['items'][0]['id']
    spotifyObject.user_playlist_add_tracks(user=username,playlist_id=playlist,tracks=ids)