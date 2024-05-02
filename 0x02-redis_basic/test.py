friends = ["imole", "david", 3.4, 3, b"kunle"]

print(str(friends))
print(friends)
print(list(map(lambda x: str(x), friends)))
# print(join)
r = redis.Redis()
print(r.get("count:https://redis.io/docs/latest/commands/expire/"))
print(get_page("https://redis.io/docs/latest/commands/expire/"))

print(r.get("https://redis.io/docs/latest/commands/expire/"))
print(r.get("count:https://redis.io/docs/latest/commands/expire/"))