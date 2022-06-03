#!/usr/bin/python3
""" sends a request to URL and displays the values of X- request-Id"""
import urllib.request
import sys

def getRequest():
    """a"""
    with urllib.request.urlopen(sys.argv[1]) as res:
        req = res.headers.get('X-Request-Id')
        print(req)

if __name__ == "__main__":
    getRequest()
