from logging import getLogger
import boto3
from helpers.Log import Log
from helpers.QiitaClient import QiitaClient

log = Log().getLogger()


def fetchAccount():
    res = QiitaClient().getMyAccount()
    if res.status_code != 200:
        log.warning(f"[Request Faild] status:{res.status_code}, {res.message}")

    return res


def createJson(data):
    pass


def putJson(json):
    pass


if __name__ == "__main__":
    res = fetchAccount()
    print(res.json())
