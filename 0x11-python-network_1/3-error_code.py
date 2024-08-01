#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
You have to manage urllib.error.HTTPError exceptions and print: Error code:
followed by the HTTP status code
"""

if __name__ == '__main__':

    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as body:
        try:
            body
        except urllib.error.HTTPError as e:
            decode_body = e.read().decode()
            print("Error code: {}".format(decode_body.code))
