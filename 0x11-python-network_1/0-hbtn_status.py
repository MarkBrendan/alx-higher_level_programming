#!/usr/bin/python3
"""A script that
- fetches https://alx-intranet.hbtn.io/status.
- uses urlib package
"""


if __name__ == '__main__':
    import urllib.request

    """request the page and open it with urlopen"""

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:

        """read the content"""

        body = r.read()

        """print out the content"""

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
