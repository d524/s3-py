import os
import requests


BASE_API_URL = "https://qiita.com/"


class QiitaClient:
    def __init__(self):
        pass

    def getMyAccount(self):
        user_id = os.environ.get("QIITA_USER", "")
        return requests.get(f"{BASE_API_URL}/api/v2/users/{user_id}")

