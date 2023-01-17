#!/usr/bin/python3
"""
Python script that takes 2 arguments
in order to solve this challenge.
"""
from requests import get, auth
import sys


if __name__ == "__main__":
    try:
        repo = sys.argv[1]
        owner = sys.argv[2]
        url = f"https://api.github.com/repos/{owner}/{repo}/commits"
        r = get(url)
        json_o = r.json()
        for i in range(0, 10):
            print("{}: {}".format(json_o[i].get('sha'), json_o[i].get('commit')
                                  .get('author').get('name')))
    except:
        pass
