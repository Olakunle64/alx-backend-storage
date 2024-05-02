#!/usr/bin/env python3
"""This module has a function named <get_page>"""
import requests
import redis


def get_page(url: str) -> str:
    """get the html content of a page and also
        keep track of how many times a url is get
    """
    r = redis.Redis()
    response = requests.get(url)
    r.incr("count:{}".format(url))
    return response.text
