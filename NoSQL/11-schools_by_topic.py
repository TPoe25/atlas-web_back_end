#!/usr/bin/env python3
"""Return schools that have a specific topic."""

from pymongo.collection import Collection
from typing import List, Dict

def schools_by_topic(mongo_collection: Collection, topic: str) -> List[Dict]:
    """
    Find schools containing the given topic in their topics list.

    Args:
        mongo_collection (Collection): The PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        List[Dict]: List of matching school documents.
    """
    return list(mongo_collection.find({"topics": topic}))
