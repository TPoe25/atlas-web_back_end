#!/usr/bin/env python3
"""
testing exercise 1
"""

from exercise import Cache

cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8"),
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    result = cache.get(key, fn=fn)
    print(f"Stored: {value!r}, Retrieved: {result!r}")
    assert result == value

key_str = cache.store("Hello")
key_int = cache.store(99)
print(cache.get_str(key_str))  # Should print "Hello"
print(cache.get_int(key_int))  # Should print 99

