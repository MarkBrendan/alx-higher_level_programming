#!/usr/bin/python3
"""A script that
- that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
- uses urlib package
"""


if __name__ == '__main__':
    import sys
    import urllib.request

    """request the page and open it with urlopen"""

    with urllib.request.urlopen(sys.argv[1]) as r:

        """get header from the url"""
        head = r.getheader("X-Request-Id")

        """print out the content"""

        print("{}".format(head))
