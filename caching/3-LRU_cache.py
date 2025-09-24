#!/usr/bin/env python3
"""
LRUCache module defines a caching system
"""

from caching.base_caching import BaseCaching

class LRUCache(BaseCaching):
    """
    LRUCache implements a Least Recently Used (LRU) caching system.
    """
    def __init__(self):
        """
        Initialize LRUCache instance.
        Calls the parent class constructor and initializes an empty list to track usage order.
        """
        super().__init__()
        self.lru_queue = []
    def put(self, key, item):
        """
        Adds an item to the cache with the specified key.

        If cache exceeds maximum number of items, it removes the least recently used item.

        Args:
            key (str): The key to associate with the item.
            item (Any): The item to be stored in the cache
        Returns: None
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.lru_queue.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discard = self.lru_queue.pop(0)
            del self.cache_data[discard]
            print("DISCARD:", discard)
        self.cache_data[key] = item
        self.lru_queue.append(key)
    def get(self, key):
        """
        Retrieves an item from the cache by key

        Args:
            key (str): The key associated with the item to retrieve.
        Returns:
            The item associated with the key, or None if the key does not exist.
        """
        if key is None or key not in self.cache_data:
            return None
        self.lru_queue.remove(key)
        self.lru_queue.append(key)
        return self.cache_data[key]
