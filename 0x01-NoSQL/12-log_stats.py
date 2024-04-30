#!/usr/bin/env python3
"""This module has a  script that provides some stats about
    Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # connnect to the MongoDB server on a localhost address
    client = MongoClient()
    logs = client.logs
    nginx = logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("{} logs".format(nginx.estimated_document_count()))
    print("Methods:")
    for method in methods:
        print("\tmethod GET: {}".format(
            nginx.count_documents({"method": method}))
            )
    print("{} status check".format(nginx.count_documents({"method": "GET", "path": "/status"})))
