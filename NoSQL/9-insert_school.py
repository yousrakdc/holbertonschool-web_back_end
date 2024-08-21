#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    docs = {}
    for k, v in kwargs.items():
        docs[k] = v
    result = mongo_collection.insert_one(docs)
    return result.new_id