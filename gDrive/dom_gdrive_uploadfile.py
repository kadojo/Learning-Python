from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


file_metadata = {'name': 'photo.jpg'}
media = MediaFileUpload('C:/Users/Dojod/Documents/Learning-Python/gDrive/photo.jpg', # MediaFileUpload is not defined (apparently)
                        mimetype='image/jpeg')
file = drive_service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
#print 'File ID: %s' % file.get('id')
