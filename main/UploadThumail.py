import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import googleapiclient.errors
from googleapiclient.http import MediaFileUpload
from PIL import Image, ImageFont, ImageDraw
# import test

#Generating the thumnail
# def genThumnail():
#     views = test.FetchViews()
#     print(views)
#     img = Image.open('components/img0.jpg')
#     font = ImageFont.truetype("arial.ttf", 100)

#     draw = ImageDraw.Draw(img)

#     text = f'Views => {views}'

#     font_color = (255, 255, 255)  # White color
#     draw.text((10, 450), text, font_color, font=font)
#     img.save('components/img1.jpg')

#Uploading Thumnail
def uploadThumail():
    VIDEO_ID = '0stJD4ttQxk' 
    thumbnail_path = 'components/img1.jpg'
    credentials_path = 'components/client.json'
    scopes = ['https://www.googleapis.com/auth/youtube.force-ssl']                    


    flow = InstalledAppFlow.from_client_secrets_file(credentials_path, scopes)       
    flow.run_local_server(host='localhost', port=8080)
    credentials = flow.credentials

    api_service_name = 'youtube'
    api_version = 'v3'
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    try:
        request = youtube.thumbnails().set(videoId=VIDEO_ID, media_body=MediaFileUpload(thumbnail_path))
        response = request.execute()

    except Exception as ex:
        print(f'error: {ex}')

uploadThumail()