import logging
import requests
from usersignup import accountcreat


class userLoggin:
    def __init__(self):
        self.token, self.id = self.usersignin()
        self.email = accountcreat().email

    def usersignin(self):
        payload = {
            "email": self.email,
            "password": "Cleveroad111"}
        res = requests.post("https://api.vottelo.dev.cleveroad.com/api/v1/sessions", json=payload, headers={
            'Content-Type': 'application/json',
            'accept': 'application/json'})
        try:
            token = res.json()['data']['session']['accessToken']
            id = res.json()['data']['user']['id']
            logging.info(f'User created! id = {id}')
            return token, id
        except Exception:
            logging.error(f'Error.Status code: {res.status_code} Response: {res.text}')
