#!/usr/bin/env python3
"""
FIFO Cache module defines a caching system that removes the oldest item
"""

from typing import Any
from caching.base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache class inherit from BaseCaching and implement FIFO caching system.
    """
    def __init__(self):
        """
        Initialize FIFOCache instance.
        """
        super().__init__()
        self.cache_data: dict[str, Any] = {}
        self.queue: list[str] = []
        self.queue = []
    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.
        If cache exceeds maximum number of items, it removes the oldest item.
        If the key already exists, it updates the item but does not change
        its position in the queue.

        Args:
            key (str): The key to associate with the item.
            item (Any): The item to be stored in the cache.

        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            return
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """
        Retrieves an item from the cache by key.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            Any: The value associated with the key, or None if the key is not found in the cache.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
