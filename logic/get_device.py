import requests
import hashlib
import hmac
import time
import json

# Stałe - te wartości musisz uzyskać z platformy Tuya IoT
CLIENT_ID = 'your-client-id'
CLIENT_SECRET = 'your-client-secret'
USERNAME = 'user@example.com'
PASSWORD = 'password'

def get_server_time():
    url = "https://openapi.tuyacn.com/v1.0/iot-01/associated-users/actions/authorized-login"
    response = requests.get(url)
    return response.json()['t']

def generate_auth_headers():
    timestamp = str(int(time.time() * 1000))  # Czas w milisekundach
    # Generowanie sygnatury
    sign_content = CLIENT_ID + timestamp
    sign = hmac.new(CLIENT_SECRET.encode('utf-8'), msg=sign_content.encode('utf-8'), digestmod=hashlib.sha256).hexdigest().upper()
    headers = {
        'client_id': CLIENT_ID,
        'sign': sign,
        't': timestamp,
        'sign_method': 'HMAC-SHA256',
    }
    return headers

def get_access_token():
    headers = generate_auth_headers()
    payload = {
        'username': USERNAME,
        'password': PASSWORD,
        'grant_type': 'password'  # Wymaga uwierzytelniania na podstawie użytkownika i hasła
    }
    url = 'https://openapi.tuyacn.com/v1.0/token?grant_type=1'
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()['result']['access_token']
    else:
        raise Exception('Failed to get access token')

def get_device_list(access_token):
    headers = {
        'client_id': CLIENT_ID,
        'access_token': access_token,
        'sign_method': 'HMAC-SHA256'
    }
    url = 'https://openapi.tuyacn.com/v1.0/users/devices'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()['result']
    else:
        raise Exception('Failed to fetch device list')

def main():
    access_token = get_access_token()
    if access_token:
        devices = get_device_list(access_token)
        print(json.dumps(devices, indent=2))  # Wypisuje listę urządzeń w formacie JSON

if __name__ == "__main__":
    main()
