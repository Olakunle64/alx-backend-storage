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
        url = str(args[0])
        r.incr("count:{}".format(url))
        if r.get(url):
            return (r.get(url).decode('utf-8'))
        result = method(*args, **kwargs)
        r.setex(url, 10, result)
        return result
    return wrapper


@cache
def get_page(url: str) -> str:
    """get the html content of a page and also
        keep track of how many times a url is get
    """
    response = requests.get(url)
    return response.text
