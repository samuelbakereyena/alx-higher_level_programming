#!/usr/bin/python3
"""sends a resquest to the url and displays the value of the x-request-id"""
import requests
from sys import argv
if __name__ == "__main__":
    if len(argv) > 1:
        q = argv[1]
    else:
        q = ""

    try:
        _data = {'q': q}
        url = 'http://0.0.0.0:5000/search_user'
        req = requests.post(url, _data).json()
        if not req:
            print("No result")
        else:
            print("[{}] {}".format(req.get('id'), req.get('name')))
    except ValueError:
        print("Not a valid JSON")

