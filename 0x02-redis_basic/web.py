#!/usr/bin/env python3
"""This module has a function named <get_page>"""
import requests
import redis
from functools import wraps


def access_track(method):
    """decorator function to keep track of the number
        of times the url is accessed
    """
    @wraps(method)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        r = redis.Redis()
        url = str(args[0])
        r.incr("count:{}".format(url))
        return method(*args, **kwargs)
    return wrapper


def web_cache(method):
    """docorator function"""
    @wraps(method)
    def wrapper(*args, **kwargs):
        """Wrapper function"""
        r = redis.Redis()
        url = str(args[0])
        if r.get(url):
            return (r.get(url).decode('utf-8'))
        result = method(*args, **kwargs)
        r.setex(url, 10, result)
        return result
    return wrapper


@access_track
@web_cache
def get_page(url: str) -> str:
    """get the html content of a page and also
        keep track of how many times a url is get
    """
    response = requests.get(url)
    return response.text
