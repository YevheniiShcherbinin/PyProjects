import requests
import time
import logging
from userlogin import userLoggin

class profile:
    def __init__(self):
        self.username = f'{round(time.time() * 1000)}' + "user"
        self.id = self.complete_profile()
        self.token = userLoggin().token

    def complete_profile(self):
        payload = {
            "username": self.username,
            "gender": "OTHER",
            "birthday": "1960-11-29T22:37:31.676Z",
            "country": "Germany",
            "region": "Berlin",
            "city": "Berlin",
            "language": "English",
            "nationality": "Afghans"}
        res = requests.post("https://api.vottelo.dev.cleveroad.com/api/v1/users / profile", json=payload, headers={
            'Authorization': 'Bearer ' + str(self.token),
            'Content-Type': 'application/json',
            'accept': 'application/json'})
        try:
            id = res.json()['user']['id']
            logging.info(f'User goals successfully created,  User if = {id}')
            return id
        except Exception:
            logging.error(f'Something went wrong. Status code: {res.status_code} Response: {res.text}')
