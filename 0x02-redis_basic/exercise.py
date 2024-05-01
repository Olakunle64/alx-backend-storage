#!/usr/bin/env python3
"""This module has a class <Cache>"""
import redis
from typing import Union
import uuid


class Cache():
    """A class with only one method."""
    def __init__(self) -> None:
        """Constructor method."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, bytes, float, str]) -> str:
        """method should generate a random key
            (e.g. using uuid), store the input data
            in Redis using the random key and return the key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
