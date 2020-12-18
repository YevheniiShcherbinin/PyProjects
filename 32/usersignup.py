import time
import requests
import logging


class accountcreat:

    def __init__(self):
        self.emailcr = round(time.time() * 1000)
        self.email = ("yevhenii.shcherbinin.cr+" + str(self.emailcr) + "@gmail.com")
        self.id = self.sign_up()

    def sign_up(self):
        payload = {
            "email": self.email,
            "password": "Cleveroad111"}
        res = requests.post('https://api.vottelo.dev.cleveroad.com/api/v1/users', json=payload, headers={
            'Content-Type': 'application/json',
            'accept': 'application/json'})
        try:
            id = res.json()['data']['id']
            logging.info(f'User created! id = {id}')
            return id
        except Exception:
            logging.error(f'Error.Status code: {res.status_code} Response: {res.text}')
