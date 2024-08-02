#!/usr/bin/python3
"""
a python script that takes in a URL and an email, sends a POST request
And passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == '__main__':

    import requests
    import sys

    url = sys.argv[1]
    mail = sys.argv[2]

    data = requets.post(url, email=mail)
    print("{}".format(data.text))
