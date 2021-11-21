import requests
import json

def getAudioFeatures(songID):
    cid = '4bb4bbafa39540db902e05b2e0d60b6a'
    secret = 'be8a2b6a8d554bacac4f8117db6e2ee4'

    authUrl = 'https://accounts.spotify.com/api/token'
    baseUrl = 'https://api.spotify.com/v1/'

    authResponse = requests.post(authUrl, {
        'grant_type' : 'client_credentials',
        'client_id' : cid,
        'client_secret' : secret
    })

    print(authResponse)

    authResponseData = authResponse.json()

    accessToken = authResponseData['access_token']

    print(accessToken)

    headers = {'Authorization': 'Bearer {token}'.format(token=accessToken)}

    response = requests.get(baseUrl + 'audio-features/' + songID, headers=headers)

    print(response)

    response = response.json()

    print(json.dumps(response))
