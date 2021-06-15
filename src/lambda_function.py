import json
import os
import urllib.request
import boto3
import logging

from secret import get_secret


level = os.environ.get('LOG_LEVEL', 'INFO')


def logger_level():
    if level == 'CRITICAL':
        return 50
    elif level == 'ERROR':
        return 40
    elif level == 'WARNING':
        return 30
    elif level == 'INFO':
        return 20
    elif level == 'DEBUG':
        return 10
    else:
        return 0


logger = logging.getLogger()
logger.setLevel(logger_level())


class Remo:
    def __init__(self, access_token: str):
        self._access_token = access_token

    def _get_api(self, path: str):
        r = urllib.request.Request(
            f'https://api.nature.global/{path}')
        r.add_header('Authorization', 'Bearer ' + self._access_token)

        with urllib.request.urlopen(r) as a:
            b = a.read()

        return json.loads(b)

    def get_devices(self):
        return self._get_api(path="/1/devices")

    def get_appliances(self):
        return self._get_api(path="/1/appliances")


class Appliance:
    def __init__(self, access_token: str, appliance_id: str):
        self._appliance_id = appliance_id
        self._access_token = access_token

    def get_signals(self):
        r = urllib.request.Request(
            f'https://api.nature.global/1/appliances/{self._appliance_id}/signals')
        r.add_header('Authorization', 'Bearer ' + self._access_token)

        with urllib.request.urlopen(r) as a:
            b = a.read()
        return json.loads(b)


def lambda_handler(event, context):
    secret = get_secret(
        region_name="ap-northeast-1",
        secret_name=os.environ.get('REMO_SECRET_NAME'))

    remo = Remo(access_token=secret['access_token'])

    logger.info(remo.get_appliances())
    logger.info(remo.get_devices()[0])

    aircon = Appliance(
        access_token=secret['access_token'],
        appliance_id=secret['aircon_appliance_id'])
    signals = aircon.get_signals()
    logger.info(signals)


lambda_handler(None, None)
