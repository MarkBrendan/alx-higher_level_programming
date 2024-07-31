#!/usr/bin/python3
"""0-hbtn_status.py module"""


import urllib.request


if __name__ == '__main__':

    """request the page and open it with urlopen"""
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:

        """read the page and print out the content"""
        body = r.read()
        print("Body response:\n\t - type: {}\n\t - content: {}\n\t - utf8 content: {}"
              .format(type(body), body, body.decode('utf-8')))
