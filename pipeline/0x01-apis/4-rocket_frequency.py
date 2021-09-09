#!/usr/bin/env python3
"""API module"""
import requests
from datetime import datetime


if __name__ == '__main__':
    url = "https://api.spacexdata.com/v4/launches/"
    req1 = requests.get(url)
    data = req1.json()
    # get all roks
    roks = requests.get("https://api.spacexdata.com/v4/rockets/").json()
    roks_id = set()
    for i in roks:
        roks_id.add(i['id'])
    b = {}
    for i in roks_id:
        rok = requests.get("https://api.spacexdata.com/v4/rockets/" +
                           i).json()
        b[i] = rok['name']

    for item in data:
        # rok = requests.get("https://api.spacexdata.com/v4/rockets/" +
        #                   item['rocket']).json()
        # print(b[item['rocket']])

        if b[item['rocket']] in dct_nbr_rocket:
            dct_nbr_rocket[b[item['rocket']]] += 1
        else:
            dct_nbr_rocket[b[item['rocket']]] = 1

    for key, value in sorted(dct_nbr_rocket.items(),
                             key=lambda item: item[1], reverse=True):
        print("{}: {}".format(key, value))
