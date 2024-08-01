#!/usr/bin/python3
"""
a python script that takes in a URL and an email, sends a POST request
And passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':

    import urllib.request
    import sys
    import urllib.parse

    url = sys.argv[1]
    mail = sys.argv[2]

    data = urllib.parse.urlencode({'email': mail})
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as body:
        decode_body = body.read().decode()
        print("{}".format(decode_body))
