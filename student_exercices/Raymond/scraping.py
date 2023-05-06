import base64
import json
import os

import requests


# https://www.kaggle.com/code/laurabarreda/extract-data-from-idealista-api

def get_oauth_token():
    '''
    This function will return our personalised token
    '''
    api_key = os.environ.get("API_KEY")  # Your API key provided by Idealista
    secret = os.environ.get("SECRET")  # Your secred code provided by Idealista

    message = api_key + ":" + secret  # Combine the API key and the secret to get our personalised message

    auth = "Basic " + base64.b64encode(message.encode("ascii")).decode("ascii")  # Encode the message

    headers_dic = {"Authorization": auth,
                   "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}  # Define our headers

    params_dic = {"grant_type": "client_credentials",  # Define the request params
                  "scope": "read"}

    r = requests.post("https://api.idealista.com/oauth/token",
                      # Perform the request with the api url, headers and params
                      headers=headers_dic,
                      params=params_dic)

    token = json.loads(r.text)['access_token']  # Obtain the personalised token, as a json

    return token


print(get_oauth_token())
