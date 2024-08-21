#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """results in changing all topics of a school"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )