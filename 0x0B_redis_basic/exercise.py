#!/usr/bin/env python3
"""
Exercise 0: Redis basics
"""

import redis
from typing import Union, Optional, Callable, Any

class Cache:
    """Cache class to interact with Redis"""

    def ___init___(self):
        """Initalize the Cache class"""
        self._redis = redis.Redis()
        self._redis.flush(db)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store data in Redis and return the key

        Args:
            data (Union[str, bytes, int, float]): The data to store
        Returns:
            str: The key under which the data is stored
        """
        key = self._redis.randomkey()
        key = f"data:{self._redis.incr('data_counter')}"
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """
        Retrieve data from Redis by key and optionally apply a conversion function

        Args:
            key (str): The key to look up in Redis
            fn (Optional[Callable]): A function to convert the data before returning
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
        value = self.get(key, lambda d: d.decode("utf-8"))
        return value

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key

        Args:
            key (str): The key to look up in Redis
        Returns:
            Optional[int]: The retrieved integer, or None if not found
        """
        value = self.get(key, int)
        return value
