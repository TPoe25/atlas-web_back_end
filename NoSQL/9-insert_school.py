#!/usr/bin/env python3
""" 9-insert school """
from typing import Any
from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs) -> Any:
    """
    Insert a new school into the given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection
        kwargs: Additional keyword arguments for the school document
    Returns:
        Any: The inserted school document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
