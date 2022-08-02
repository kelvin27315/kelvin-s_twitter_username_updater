import datetime as dt
from os import environ

import requests
from requests_oauthlib import OAuth1Session


def make_username() -> str:
    target_date = dt.date(2022, 9, 11)
    days = str(target_date - dt.date.today()).split()[0]
    if days == "0:00:00":
        days = "0"
    username = "けるびん❀紅茶会(求14)残" + days + "日"
    return username


def create_session() -> OAuth1Session:
    access_token = environ.get("ACCESS_TOKEN")
    access_token_secret = environ.get("ACCESS_TOKEN_SECRET")
    consumer_api_key = environ.get("CONSUMER_API_KEY")
    consumer_api_key_secret = environ.get("CONSUMER_API_KEY_SECRET")

    session = OAuth1Session(consumer_api_key, consumer_api_key_secret, access_token, access_token_secret)
    return session


def print_error(req: requests.models.Response) -> None:
    print("Status code: {}".format(req.status_code))
    print("Error message: {}".format(req.text))


def update_username(username: str) -> None:
    url = "https://api.twitter.com/1.1/account/update_profile.json"
    params = {"name": username}

    session = create_session()
    req = session.post(url, params=params)
    if req.status_code != 200:
        print_error(req)


def main() -> None:
    username = make_username()
    update_username(username)


if __name__ == "__main__":
    main()
