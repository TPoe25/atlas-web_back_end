#!/usr/bin/env python3
""" insert_school module to insert a school into a MongoDB collection."""
from typing import Any
from pymongo.collection import Collection

"""Insert a school into a MongoDB collection."""

from typing import Any
from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs) -> Any:
    """Insert a new school into the given MongoDB collection.

    Args:
        mongo_collection (Collection): The PyMongo collection object.
        **kwargs: Arbitrary key-value pairs for the school document.

    Returns:
        Any: The _id of the newly inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
