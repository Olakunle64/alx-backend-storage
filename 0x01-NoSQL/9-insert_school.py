#!/usr/bin/env python3
"""This module has a function name <insert_school> that
    inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """This function inserts a new document in a collection
        based on kwargs

        Args:
            mongo_collection: collection
            kwargs: a dictionary

        Return: return the new _id.
    """
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id

