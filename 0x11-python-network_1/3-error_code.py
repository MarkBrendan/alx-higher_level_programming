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
    import urllib.error

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as body:
            decode_body = body.read().decode('UTF-8')
            print("{}".format(decode_body))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
