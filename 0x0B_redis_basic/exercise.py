#!/usr/bin/env python3
"""
Exercise 0: Redis basics
"""

import redis
import uuid
from typing import Union, Optional, Callable, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that increments Redis counter and calls method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator that stores teh history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # create keys for inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # store input args
        self._redis.rpush(input_key, str(args))

        # call the actual methond to get its result
        result = method(self, *args, **kwargs)

        # Store output result
        self._redis.rpush(output_key, str(result))

        # Return the actual result
        return result
    return wrapper


class Cache:
    """Cache class to interact with Redis"""

    def __init__(self):
        """Initalize the Cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key

        Args:
            data (Union[str, bytes, int, float]): The data to store
        Returns:
            str: The key under which the data is stored
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis by key, optionally applys conversion function

        Args:
            key (str): The key to look up in Redis
            fn (Optional[Callable]): Function to convert data before returning
        Returns:
            Any: The retrieved data, possibly converted by fn
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis by key

        Args:
            key (str): The key to look up in Redis
        Returns:
            Optional[str]: The retrieved string, or None if not found
        """
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key

        Args:
            key (str): The key to look up in Redis
        Returns:
            Optional[int]: The retrieved integer, or None if not found
        """
        return self.get(key, int)


def replay(method: Callable) -> None:
    """
    Display the history of calls of a particular function.

    Example:
        >>> cache = Cache()
        >>> cache.store("foo")
        >>> cache.store("bar")
        >>> replay(cache.store)
        Cache.store was called 2 times:
        Cache.store(*('foo',)) -> <uuid>
        Cache.store(*('bar',)) -> <uuid>

    """
    redis_instance = method.__self__._redis
    method_name = method.__qualname__

    inputs = redis_instance.lrange(f"{method_name}:inputs", 0, -1)
    outputs = redis_instance.lrange(f"{method_name}:outputs", 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_data, output_data in zip(inputs, outputs):
        print(f"{method_name}(*{input_data.decode
              ('utf-8')}) -> {output_data.decode('utf-8')}")
