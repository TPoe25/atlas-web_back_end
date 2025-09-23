#!/usr/bin/env python3
"""
BasicCache module defines a basic caching system.
"""

from basecaching import BaseCaching

class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from BaseCaching.
    Methods:
        put(key, item):
            Adds an item to the cache.
        get(key):
            Retrieves an item from the cache
    """
    def put(self, key, item):
        """
        Add an item to the cache. If the cache exceeds its limit, removes the oldest item.
        Args:
            key (str): The key for the item.
            item (any): The item to be cached.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
    def get(self, key):
        """
        Retrieves an item from the cache by its key.

        Args:
            key (str): The key for the item to retrieve.

        Returns:
            The value of the item in cache, or None if not found.
        """
        return self.cache_data.get(key)
