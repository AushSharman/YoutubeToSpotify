import requests
import json
import base64 as b64
client_id = "c5ef9d7880554bd88d0b4d53e718eb1b"
client_secret = "2770de74afce48bd85e68944324f8979"
URL = "https://account.spotify.com/api/token"

# pass base64 encoded creds to pass into request param
client_creds = f"{client_id}:{client_secret}".encode()

"""do a lookup for my token so that access for future is permitted"""
PARAMS = {
    "grant_type": "client_credentials"
}
HEADER = {
    "Authorization" : f"Basic {b64.b64encode(client_creds)}"
}


print(client_creds)



