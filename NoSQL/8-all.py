#!/usr/bin/env python3
"""lists all documents in a collection"""

def list_all(mongo_collection):
    """Return an empty list if no document in the collection"""
    docs = mongo_collection.find()
    result = []
    for doc in docs:
        result.append(doc)
    return result