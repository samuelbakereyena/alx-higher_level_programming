#!/usr/bin/python3
"""sends a request to the URL AND VALUE OF THE x- rEQUEST-iD"""
    import requests
    from sys import argv


if __name__ == "__main__":
    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
