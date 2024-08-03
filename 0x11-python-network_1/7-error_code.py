#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to
the URL and displays the body of the response.
"""

if __name__ == '__main__':

    import requests
    import sys

    url = sys.argv[1]

    resp = requests.get(url)
    resps = resp.text
    if resps.status_code >= 400:
        print("Error code: {}".format(resps.status_code))
