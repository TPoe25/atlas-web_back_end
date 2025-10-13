#!/usr/bin/env python3
"""Update topics for a school in a MongoDB collection."""

from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Update the topics of a school identified by name.

    Args:
        mongo_collection (Collection): The PyMongo collection object.
        name (str): The name of the school to update.
        topics (List[str]): List of topics to set for the school.
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
