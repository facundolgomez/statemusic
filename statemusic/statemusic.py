import requests
import os
from dotenv import load_dotenv


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


get_token()

print(TOKEN)
