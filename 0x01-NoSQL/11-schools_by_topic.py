#!/usr/bin/env python3
"""This module has a function named <schools_by_topic> that
    returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """This function returns the list of school having
        a specific topic

        Args:
            mongo_collection: collection
            topic: a string

        Return: return a list of school having the specific topic
    """
    return mongo_collection.find({"topics": {"$in": [topic]}})
