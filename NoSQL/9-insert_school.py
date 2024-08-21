#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
from pymongo import InsertOne


def insert_school(mongo_collection, **kwargs):
    """Returns the new _id"""
    docs = {}
    for i, j in kwargs.items():
        docs[i] = j
    result = mongo_collection.insert_one(docs)
    return result.new_id