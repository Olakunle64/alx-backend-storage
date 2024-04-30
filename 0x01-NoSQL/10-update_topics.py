#!/usr/bin/env python3
"""This module has a function named <update_topics> that
    changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
    """This function changes all topics of a school document
        based on the name

        Args:
            mongo_collection: collection
            name: string
            topics: list of string

        Return: void.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
