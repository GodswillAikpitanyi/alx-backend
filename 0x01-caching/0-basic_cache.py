#!/usr/bin/python3
""" Defines Class Basic Cache """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represents an object that allows storing and
         retrieving items from a dictionary.
    """
    def put(self, key, item):
        """ Adds data to the cache
        """
        if key is None or item is None:
            pass
        self.cache_data[key] = item


    def get(self, key):
        """Retrieves an item by key.
        """
        return self.cache_data.get(key, None)