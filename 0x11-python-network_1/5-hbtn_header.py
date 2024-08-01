#!/usr/bin/python3
"""A script that
- that takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response.
- uses requests package
"""


if __name__ == '__main__':
    import sys
    import requests

    resp = requests.get(sys.argv[1])

    """get header from the url"""
    head = resp.headers.get("X-Request-Id")

    """print out the content"""
    print("{}".format(head))
