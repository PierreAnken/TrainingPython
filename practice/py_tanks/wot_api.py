import json
import os
import requests
from requests import RequestException
import logging


class WotAPI:

    # https://developers.wargaming.net/reference/

    BASE_API_URL = 'https://api.worldoftanks.eu/wot/'
    WOT_APP_ID = os.environ.get("wot_app_id")

    def get_tank_list(self, tiers=None):

        if tiers is None:
            tiers = range(11)
        tiers = json.dumps(tiers)

        url = f'{self.BASE_API_URL}/encyclopedia/vehicles/?application_id={self.WOT_APP_ID}&language=fr&tier={tiers}'
        req_get_tanks = requests.get(url)
        data_json = req_get_tanks.json()

        status = data_json.get('status')
        if status != 'ok':
            raise RequestException(f'The following request failed {url} with status {status}')
        logging.info(f'Successful request {url}')
        return data_json.get('data')
