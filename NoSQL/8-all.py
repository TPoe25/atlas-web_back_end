#!/usr/bin/env python3
""" 8-all.py: List all docs in a collection"""

def list_all(mongo_collection):
    """
    List all documents in a given MongoDB collection.

    Args:
        mongo_collection (pymongo.collection.Collection): The PyMongo collection
    Returns:
        list: A list of all documents in the collection
    """
    if mongo_collection is None:
        return []

    # Fetch documents from collection and convert them to a list
    return list(mongo_collection.find())
