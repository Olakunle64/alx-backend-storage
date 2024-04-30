#!/usr/bin/env python3
"""This module has a function named <list_all> that lists
    all documents in a collection
"""


def list_all(mongo_collection):
    """This function lists all documents in a collections

        Args:
            mongo_collection: collection just like
                                table in RDBMS
    """
    if not mongo_collection.estimated_document_count():
        return []
    return mongo_collection.find()
