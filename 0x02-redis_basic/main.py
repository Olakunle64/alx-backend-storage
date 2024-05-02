# #!/usr/bin/env python3
# """
# Main file
# """
# import redis

Cache = __import__('exercise').Cache

# cache = Cache()

# data = b"hello"
# key = cache.store(data)
# print(key)

# local_redis = redis.Redis()
# print(local_redis.get(key))

# # task 1
# cache = Cache()

# TEST_CASES = {
#     b"foo": None,
#     123: int,
#     "bar": lambda d: d.decode("utf-8")
# }

# for value, fn in TEST_CASES.items():
#     key = cache.store(value)
#     assert cache.get(key, fn=fn) == value


# # task 2

# Cache = __import__('exercise').Cache

# cache = Cache()

# cache.store(b"first")
# print(cache.get(cache.store.__qualname__))

# cache.store(b"second")
# cache.store(b"third")
# print(cache.get(cache.store.__qualname__))

# # Task 3
# Cache = __import__('exercise').Cache

# cache = Cache()

# s1 = cache.store("first")
# print(s1)
# s2 = cache.store("secont")
# print(s2)
# s3 = cache.store("third")
# print(s3)

# inputs = cache._redis.lrange("{}:inputs".format(cache.store.__qualname__), 0, -1)
# outputs = cache._redis.lrange("{}:outputs".format(cache.store.__qualname__), 0, -1)

# print("inputs: {}".format(inputs))
# print("outputs: {}".format(outputs))

def replay(method):
    import redis
    """display the call history"""
    r = redis.Redis()
    inputs = r.lrange("{}:inputs".format(method.__qualname__), 0, -1)
    outputs = r.lrange("{}:outputs".format(method.__qualname__), 0, -1)
    print("{} was called {} times:".format(method.__qualname__, len(outputs)))
    for in_out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method.__qualname__, in_out[0].decode("utf-8"), in_out[1].decode("utf-8")))

cache = Cache()
cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)