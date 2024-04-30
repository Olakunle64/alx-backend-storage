#!/usr/bin/env python3
"""This module has a function named <top_students> that
    returns all students sorted by average score
"""


def top_students(mongo_collection):
    """This function returns all students sorted by average score

        Args:
            mongo_collection: collection
    """
    return mongo_collection.aggregate([
        {"$addFields": {"averageScore": {"$avg": "$topics.score"}}},
        {"$sort": {"averageScore": -1}}
    ])
