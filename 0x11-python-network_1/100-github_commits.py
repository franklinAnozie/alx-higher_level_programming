#!/usr/bin/python3
""" Technical Interview: Get the username and commits to a repo"""

import requests
import sys


def get_req(repo, user):
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    limit = {"per_page": 10}

    response = requests.get(url, params=limit)

    if response.status_code == 200:
        for resp in response.json():
            print(f"{resp.get('sha')}: {resp.get('commit').get('author').get('name')}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <repository name> <owner name>")
    else:
        repo = sys.argv[1]
        user = sys.argv[2]
        get_req(repo, user)
