import requests
import os
import webbrowser
from dotenv import load_dotenv
from urllib.parse import urlencode
import time


load_dotenv(dotenv_path="credentials.env")

TOKEN = None

url_token = "https://accounts.spotify.com/api/token"

headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

data = {
	"grant_type": "client_credentials",
	"client_id": os.getenv("SPOTIFY_CLIENT_ID"),
	"client_secret": os.getenv("SPOTIFY_CLIENT_SECRET")
}

def get_token():
	global TOKEN
	response = requests.post(url_token, headers=headers, data=data)
	result = response.json()
	TOKEN = result.get("access_token")


def get_authorization():
	
    
    params = {
		"response_type": 'code',
		"client_id": os.getenv("SPOTIFY_CLIENT_ID"),
		"redirect_uri": "http://127.0.0.1:8888/callback",
		"state": "state"
	}
    url = "https://accounts.spotify.com/authorize?" + urlencode(params)
    
    
   
    webbrowser.open(url)
    while not os.path.exists("code.txt"):
        time.sleep(1)
    
    with open("code.txt", "r") as f:
        code = f.read().strip()	
    

    

if __name__ == "__main__":
	get_token()
	get_authorization()
	
	
	

