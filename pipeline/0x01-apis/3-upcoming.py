#!/usr/bin/env python3
"""API module"""
import requests
from datetime import datetime


if __name__ == '__main__':
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    req1 = requests.get(url)
    data = req1.json()
    data.sort(key=lambda json: json['date_unix'])
    data = data[0]

    v_name = data["name"]

    v_localtime = data["date_local"]

    # <rocket name>
    rock_url = "https://api.spacexdata.com/v4/rockets/" + data["rocket"]
    req3 = requests.get(rock_url)
    rock_data = req3.json()
    v_rock_name = rock_data['name']

    # <launchpad name> (<launchpad locality>)
    launchpad_url = "https://api.spacexdata.com/v4/launchpads/" +\
        data["launchpad"]
    req2 = requests.get(launchpad_url)
    launch_data = req2.json()
    v_launch_name = launch_data['name']
    v_lauch_local = launch_data['locality']

    print("{} ({}) {} - {} ({})".format(v_name, v_localtime,
                                        v_rock_name, v_launch_name,
                                        v_lauch_local))
