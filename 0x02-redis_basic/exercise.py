#!/usr/bin/env python3
"""This module has a class <Cache>"""
import redis
from typing import Union
import uuid
from functools import wraps
from typing import Callable


def count_calls(method: Callable) -> Callable:
    """Decorator that takes a method and returns a new method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that takes a method and returns a new method"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper method"""
        key_input = "{}:inputs".format(method.__qualname__)
        self._redis.rpush(key_input, str(args))
        output = method(self, *args, **kwargs)
        key_output = "{}:outputs".format(method.__qualname__)
        self._redis.rpush(key_output, output)
        return output
    return wrapper


def replay(method):
    """display the call history"""
    r = redis.Redis()
    inputs = r.lrange("{}:inputs".format(method.__qualname__), 0, -1)
    outputs = r.lrange("{}:outputs".format(method.__qualname__), 0, -1)
    print("{} was called {} times:".format(method.__qualname__, len(outputs)))
    for in_out in zip(inputs, outputs):
        print(
            "{}(*{}) -> {}".format(
                method.__qualname__, in_out[0].decode("utf-8"),
                in_out[1].decode("utf-8")
                )
            )


class Cache():
    """A class with only one method."""
    def __init__(self) -> None:
        """Constructor method."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[int, bytes, float, str]) -> str:
        """method should generate a random key
            (e.g. using uuid), store the input data
            in Redis using the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: callable = None):
        """method should obtain the value stored in Redis
            for a given key and return it. The get method
            should return the data as the correct type
            (int, float, str, etc.), if the user
            provided a fn argument
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """method should obtain the value stored in Redis
            for a given key and return it as a string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """method should obtain the value stored in Redis
            for a given key and return it as an integer
        """
        return self.get(key, int)
