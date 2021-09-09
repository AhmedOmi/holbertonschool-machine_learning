#!/usr/bin/env python3
"""API module"""
import requests


def sentientPlanets():
    """
    ist of planets name of all sentinent species
    """
    url = "https://swapi-api.hbtn.io/api/species/"
    r = requests.get(url)
    c = r.json()
    planets = list()
    while True:
        results = c['results']
        for sentinent in results:
            planet_url = sentinent['homeworld']
            if planet_url:
                name = requests.get(planet_url).json()['name']
                planets.append(name)
        if c['next'] is None:
            break
        r = requests.get(c['next'])
        c = r.json()
    return planets
