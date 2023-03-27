

"""

Simple 2018 100 Albums extractor


"""

import spotipy
import csv
import pandas as pd
# import boto3
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

cid=os.environ.get('cid')
csecret=os.environ.get('csecret')






spotify=spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=cid,client_secret=csecret))


album_dict= {
    "Year": [],
    "Album Length": [],
    "Album Name": [],
    "Artist": []
    
    
    
}



def get_artists_from_playlist(playlist_uri):
    '''
    :param playlist_uri: Playlist to analyse
    :return: A dictionary(artist uri : artist name) of all primary artists in a playlist.
    '''
    artists = {}
    # print(playlist_uri)
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)
    for song in playlist_tracks['items']:
        if song['track']:
            # print(song['track']['artists'][0]['name'])
            artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    # return artists
    return playlist_tracks


tracks=get_artists_from_playlist("spotify:playlist:37i9dQZEVXcF7HHH4pWZHq")

playlist=[]
artist=[]
album=[]


for track in tracks['items']:
    print(track['track']['uri'])
    # print(track['track'].keys())
    print(track['track']['album'].keys())
    print(track['track']['album']['name'])
    playlist.append(track['track']['name'])
    artist.append(track['track']['artist'][0]['name'])
    album.append(track['track']['album'][0]['name'])
    

# print(playlist)

# print(get_artists_from_playlist("spotify:playlist:37i9dQZEVXcF7HHH4pWZHq"))

# mg_uri="spotify:artist:60d24wfXkVzDSfLS6hyCjZ"


# #send a request to get all his albulms
# artist=spotify.artist(mg_uri)
# print(artist)
# genre=artist['genres']
# results=spotify.artist_albums(mg_uri,album_type="album")
#loop through the first 1000 tracks of 2018


# albums=[]
# artist=[]
# track=[]
# release_date=[]
# number_of_tracks=[]
# album_id=[]


# for i in range(10):
#     track_results=spotify.search(q="year:2018",type="album")
#     print(track_results)
    
#     for i,t in enumerate(track_results['albums']['items']):
#         artist.append(t['artists'][0]['name'])
#         track.append(t['name'])
#         album_id.append(t['id'])
#         release_date.append(t['release_date'])
#         number_of_tracks.append(t['total_tracks'])
        
        
       
# #load them into a dataframe
# tracks_2018=pd.DataFrame({'album_id':album_id,'artist':artist,'album':track,'number_of_tracks':number_of_tracks,'release_date':release_date}) 
    
# print(tracks_2018)   
    
    
# print(albums[0])
# print(set(artist))


# print(results)
# albums=results['items']

# while results['next']:
#     results=spotify.next(results)
#     albums.extend(results['items'])
    
# for album in albums:
#     print(album['name'])




# # https://open.spotify.com/album/6yaDQvusuMpB2BqrsmhSRI?si=XbnCNT5oQxO6_3cwciEY1g
# # https://open.spotify:37i9dQZF1E3554p10SfBaR
# def spotify_playlist():
#     playlists={"Daiy_Mix_1":"spotify:37i9dQZF1E3554p10SfBaR" }
#     return playlists


# # https://open.spotify.com/playlist/37i9dQZF1DZ06evO3R5f8c?si=ca8d079311ed4156
# def personal_playlist():
#     playlist={"This_is_Blac_Coffee": "spotify:playlist:37i9dQZF1DZ06evO3R5f8ct"}
#     return playlist

# playlist=None

# def gather_data_local():
    
#     with open


