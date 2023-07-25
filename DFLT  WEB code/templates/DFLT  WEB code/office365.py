from onedrivesdk import OneDriveClient
from onedrivesdk.helpers import GetAuthCodeServer

redirect_uri = 'http://localhost:8080/'
client_id = 'your_client_id'
client_secret = 'your_client_secret'
scopes=['wl.signin', 'wl.offline_access', 'onedrive.readwrite']

http_provider = onedrivesdk.HttpProvider()
auth_provider = onedrivesdk.AuthProvider(
    http_provider=http_provider,
    client_id=client_id,
    scopes=scopes)

client = OneDriveClient('https://api.onedrive.com/v1.0/', auth_provider, http_provider)
auth_url = client.auth_provider.get_auth_url(redirect_uri)

# this will block until we have the code
code = GetAuthCodeServer.get_auth_code(auth_url, redirect_uri)
client.auth_provider.authenticate(code, redirect_uri, client_secret)

# read a file
filename = 'test.txt'
returned_item = client.item(drive='me', id='root').children[filename].get()
print('Received file: ' + returned_item.name)
