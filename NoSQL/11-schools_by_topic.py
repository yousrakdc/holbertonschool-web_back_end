#!/usr/bin/env python3
"""returns the list of school having a specific topic"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    return list(mongo_collection.find({"topics": topic}))