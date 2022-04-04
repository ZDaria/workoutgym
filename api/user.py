import requests
from requests import Session
import json
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:5000/api/user"
user = 'Jack'
password = 'Jones'

hostname = "127.0.0.1:5000/"
session = Session()
session.auth = (user, password)


def main():

    res = requests.get(url)

    if res.status_code == 200:
        print(res.status_code)
    else:
        print(res.status_code)


if __name__ == "__main__":
    main()
