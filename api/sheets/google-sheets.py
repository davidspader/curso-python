
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
# modificar tirando o .readonly do final
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# escolher a planilha que quer conectar e um range só para conferir se conectou
SAMPLE_SPREADSHEET_ID = '1VPuEQ9guU7RuEOIZ3kWMsuzmqGBXbGopIadYCjdNQkg'
SAMPLE_RANGE_NAME = 'Página1!A1:A5'

credentials = os.getcwd() + '/api/sheets/credentials.json'


"""Shows basic usage of the Sheets API.
Prints values from a sample spreadsheet.
"""
creds = None
# The file token.json stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
if os.path.exists('token.json'):
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials, SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.json', 'w') as token:
        token.write(creds.to_json())

service = build('sheets', 'v4', credentials=creds)

# Call the Sheets API
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range=SAMPLE_RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print("Conexão Bem sucedida")

# Pegar valores de um conjunto do celula
sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                            range='Página1!A1:B5').execute()
values = result.get('values', [])
print(values)

# Escrever valores
values = [
    [
        "david"
    ],
]
body = {
    'values': values
}
result = service.spreadsheets().values().update(
    spreadsheetId=SAMPLE_SPREADSHEET_ID, range="Página3!A1", valueInputOption="RAW", body=body
).execute()
print('{0} cells updated'.format(result.get('updatedCells')))