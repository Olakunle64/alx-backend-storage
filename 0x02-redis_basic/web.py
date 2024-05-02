#!/usr/bin/env python3
"""This module has a function named <get_page>"""
import requests
import redis
from functools import wraps


def cache(method):
    """docorator function"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        r = redis.Redis()
        result = method(*args, **kwargs)
        url = str(args[0])
        if r.get("count:{}".format(url)):
            newCount = int(r.get("count:{}".format(url))) + 1
        else:
            newCount = 1
        r.set("count:{}".format(url), newCount, ex=10)
        return result
    return wrapper


@cache
def get_page(url: str) -> str:
    """get the html content of a page and also
        keep track of how many times a url is get
    """
    response = requests.get(url)
    return response.text
