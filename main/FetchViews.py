import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload

def getViews():
    # https://www.youtube.com/watch ?v=0stJD4ttQxk
    VIDEO_ID = '0stJD4ttQxk' 
    thumbnail_path = 'components/img5.jpg'
    credentials_path = 'components/client.json'

    '''
    Defines the OAuth 2.0 scopes required for accessing the YouTube API. 
    In this case, it grants permission for read-only access to YouTube data.
    what is OAuth 2.0? -> It's a system that allows for Authentication to be relegated to another party
    '''
    scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']               
    
    '''
    Below line initiates the OAuth 2.0 authentication flow 
    using the client secrets stored in the client.json file and the specified scopes.
    '''
    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)        # Get credentials and create an API client


    '''
    below function call starts a local web server to handle the OAuth 2.0 callback. The user will be
    prompted to authorize the application, and upon successful authorization, the flow will continue.
    '''
    flow.run_local_server(host='localhost', port=8080)

    '''
    After the user authorizes the application, below line retrieves the OAuth 2.0 credentials 
    (access token, refresh token, etc.) needed to authenticate requests to the YouTube API.
    '''
    credentials = flow.credentials


    api_service_name = 'youtube'
    api_version = 'v3'

    '''
    Create an instance of youtube API and it retireves  the OAuth 2.0 credentials (access token, refresh token, etc.) 
    needed to authenticate requests to the YouTube API.
    '''
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    

    try:
        # Request to retrieve video details including views
        video_response = youtube.videos().list(part='snippet,statistics', id=VIDEO_ID).execute()
            # print(video_response)     
        views = video_response['items'][0]['statistics']['viewCount']
        return views

    except Exception as ex:
        print(f'error: {ex}')
    
