#!/usr/bin/python3
"""sends a request to the URL AND VALUE OF THE x- rEQUEST-iD"""
    import requests
import sys


if __name__ == "__main__":
    try:
        response = requests.get(sys.argv[1])
        print(response.headers.get('X-Request-Id'))
    except:
        pass
