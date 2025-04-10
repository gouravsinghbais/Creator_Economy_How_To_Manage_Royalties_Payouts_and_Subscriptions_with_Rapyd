import os
import time
import json
import hmac
import base64
import hashlib
import requests
from dotenv import load_dotenv

load_dotenv()

access_key = os.getenv("RAPYD_ACCESS_KEY")
secret_key = os.getenv("RAPYD_SECRET_KEY")
base_url = "https://sandboxapi.rapyd.net"

def generate_signature(http_method, url_path, salt, timestamp, body=''):
    body_str = json.dumps(body, separators=(',', ':')) if body else ''
    to_sign = f'{http_method}{url_path}{salt}{timestamp}{access_key}{secret_key}{body_str}'
    h = hmac.new(secret_key.encode(), to_sign.encode(), hashlib.sha256)
    return base64.b64encode(h.digest()).decode()

def make_rapyd_request(method, path, body=None):
    salt = os.urandom(12).hex()
    timestamp = str(int(time.time()))
    signature = generate_signature(method, path, salt, timestamp, body)

    headers = {
        "access_key": access_key,
        "salt": salt,
        "timestamp": timestamp,
        "signature": signature,
        "Content-Type": "application/json"
    }

    response = requests.request(method, base_url + path, headers=headers, json=body)
    return response.json()
