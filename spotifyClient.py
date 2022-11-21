import requests
import base64
import os

class SpotifyClient:
  
  def getAccessToken(self):
    URL = "https://accounts.spotify.com/api/token"
    my_secret = os.environ['clientSecret']
    credentials = "{0}:{1}".format("fc11a414fad2499ba6680e2ac3a5b517", my_secret)
    credentials_bytes = credentials.encode('ascii')
    base64_credentials = base64.b64encode(credentials_bytes).decode('ascii')
    
    HEADERS = {"Authorization": "Basic " + base64_credentials, "Content-Type": "application/x-www-form-urlencoded"}               
    BODY = {"grant_type": "client_credentials"}
  
    r = requests.post(url = URL, headers = HEADERS, data = BODY)
  
    return r.json()["access_token"]

  
  def getSpotifyPlaylistBySpotifyId(self, spotifyId):
    URL = "https://api.spotify.com/v1/playlists/{}".format(spotifyId)
    HEADERS = {"Content-Type": "application/json", "Authorization": "Bearer {}".format(self.getAccessToken())}        
  
    r = requests.get(url = URL, headers = HEADERS)
  
    return r.json()["tracks"]["items"][0]
    
    
  