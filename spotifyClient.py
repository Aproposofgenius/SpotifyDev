import requests
import base64

class SpotifyClient:
  
  def getAccessToken(self):
    URL = "https://accounts.spotify.com/api/token"
    message = "{0}:{1}".format("fc11a414fad2499ba6680e2ac3a5b517", "dummySecret")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    
    HEADERS = {"Authorization": "Basic " + base64_message, "Content-Type": "application/x-www-form-urlencoded"}               
    BODY = {"grant_type": "client_credentials"}
  
    r = requests.post(url = URL, headers = HEADERS, data = BODY)
  
    return r.json()["access_token"]