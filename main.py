import os

import requests
import base64
from dotenv import load_dotenv

load_dotenv(
    verbose=True,
    override=True,
    dotenv_path='.env'
)

CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
def get_auth_token():
    response = requests.post(
        url='https://sandbox-auth-api.mypos.com/oauth/token',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic %s' % base64.b64encode(
                f'{CLIENT_ID}:{CLIENT_SECRET}'.encode('utf-8')).decode()
        },
        data=dict(
            grant_type='client_credentials'
        )
    )


    return response

if __name__ == '__main__':
    response = get_auth_token()
    print(response.status_code)
    print(response.json())