#!/usr/bin/env python3
"""changes all topics of a school document based on the name"""
from pymongo import MongoClient


def update_topics(mongo_collection, name, topics):
    """return what's asked"""
    filter_query = {"name": name}
    update_operation = { '$set': {"topics": topics} }
    result = mongo_collection.update_one(filter_query, update_operation)
    
    return result.matched_count, result.modified_count