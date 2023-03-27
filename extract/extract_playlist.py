import spotipy
import csv
import pandas as pd
# import boto3
from datetime import datetime
import os
from dotenv import load_dotenv
from tqdm import tqdm as tq


load_dotenv()

cid=os.environ.get('cid')
csecret=os.environ.get('csecret')



spotify=spotipy.Spotify(client_credentials_manager=spotipy.oauth2.SpotifyClientCredentials(client_id=cid,client_secret=csecret))


_Playlist="Discover_Weekly"



def get_songs_from_playlist(playlist_uri):
    '''
    :param playlist_uri: Playlist to analyse
    :return: A dictionary(artist uri : artist name) of all primary artists in a playlist.
    '''
    artists = {}
    # print(playlist_uri)
    playlist_tracks = spotify.playlist_tracks(playlist_id=playlist_uri)
    # for song in playlist_tracks['items']:
    #     if song['track']:
    #         # print(song['track']['artists'][0]['name'])
    #         artists[song['track']['artists'][0]['uri']] = song['track']['artists'][0]['name']
    return playlist_tracks

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
    return artists


def spotify_playlists():
    
    # spotify:playlist:37i9dQZEVXcF7HHH4pWZHq
    playlists={"Daily_Mix_1":"spotify:playlist:37i9dQZF1E3554p10SfBaR",
               "Discover_Weekly": "spotify:playlist:37i9dQZEVXcF7HHH4pWZHq"}
    return playlists



def gather_data_local():
    album_dict= {
    
    "Album_id": [],
    "Artist": [],
    "Album Name": [],
    "Genre":[],
    "Artist Followers": [],
    "Popularity": [],
    "Album Popularity": [],
    "Year": [],    
    "Album Length": [],
    "Song Duration": []
    
    
    
    
        }
    with open("../data/Discover_Weekly.csv","w") as file:
        header = list(album_dict.keys())
        writer = csv.DictWriter(file,fieldnames=header)
        writer.writeheader()
        
        albums=[]
        
        artists=get_artists_from_playlist(spotify_playlists()[_Playlist])
        playlist_tracks=get_songs_from_playlist(spotify_playlists()[_Playlist])
       
        for index, artist_prof in enumerate(tq(list(artists.keys()),desc="Extracting data")):
          
        
            artist_profile=spotify.artist(artist_prof)  
            album=playlist_tracks['items'][index]
       
            album_id=album['track']['uri']
            writer.writerow({'Album_id': album_id,
                                        'Artist':album['track']['artists'][0]['name'],
                                        'Album Name': album['track']['name'],
                                        'Genre': artist_profile['genres'],
                                        'Artist Followers': artist_profile['followers']['total'],
                                        'Popularity': artist_profile['popularity'], 
                                        'Album Popularity':album['track']['popularity'],
                                                                         
                            'Year': album['track']['album']['release_date'],
                                            'Album Length': album['track']['track_number'],
                                            'Song Duration': album['track']['duration_ms']
                                            
                                            })
                # # album_id=tracks['uri']
                # album_dict['Album_id'].append(album_id)
                # album_dict['Album Length'].append(album['track']['track_number'])
                # album_dict['Artist'].append(album['track']['artists'][0]['name'])
                # # album_dict['Artist_uri'].append(album['artist'][0]['uri'])
                # album_dict['Album Name'].append(album['track']['name'])
                # album_dict['Year'].append(album['track']['album']['release_date'])
                
            
            
        
   

    return album_dict


gather_data_local()