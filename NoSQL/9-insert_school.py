#!/usr/bin/env python3
"""inserts a new document in a collection based on kwargs"""
from pymongo import MongoClient

def insert_school(mongo_collection, **kwargs):
    """The _id of the newly inserted document."""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id