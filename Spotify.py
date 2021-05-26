import requests
import base64

AUTHORIZE_URL = "https://accounts.spotify.com/authorize"
API_TOKEN_URL = "https://accounts.spotify.com/api/token"

AUTH_PARAMS = {
    "client_id" : f"c5ef9d7880554bd88d0b4d53e718eb1b",
    "response_type" : f"code",
    "redirect_uri" : f"http://localhost:8888/",
    "scope" : " ".join(
        [
            "playlist-modify-public", "playlist-modify-private", "playlist-read-private"
        ]
    )
}

TOKEN_PARAMS = {
    "grant_type" : "authorization_code",
    "code" : "PASS",
    "redirect_uri" : "http://localhost:8888/"
}

TOKEN_HEADER = {
    "Authorization" : "Basic <base64 encoded "
}
response = requests.get(AUTHORIZE_URL, params=AUTH_PARAMS)

print(response.url)
print(response.status_code)
print(response.text)

#TODO: 