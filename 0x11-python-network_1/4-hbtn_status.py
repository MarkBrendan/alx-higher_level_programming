#!/usr/bin/python3
"""
A script that fetches a url https://alx-intranet.hbtn.io/status
using the requests package
"""

if __name__ == '__main__':

    import requests

    resp = requests.get('https://alx-intranet.hbtn.io/status')

    print("Body response:")
    print("\t- type: {}".format(type(resp.text)))
    print("\t- content: {}".format(resp.text))
