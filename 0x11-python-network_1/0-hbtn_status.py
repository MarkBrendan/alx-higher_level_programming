#!/usr/bin/python3

import urllib.request


if __name__ == '__main__':
    
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        body = r.read()
        print("Body response:")
        print("\t - type: {}\n \t - content: {}\n \t - utf8 content: {}"
                .format(type(body), body, body))
