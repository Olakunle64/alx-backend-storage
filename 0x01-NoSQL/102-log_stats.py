#!/usr/bin/env python3
"""Improve 12-log_stats.py by adding the top 10 of the most present
    IPs in the collection nginx of the database logs
"""
from pymongo import MongoClient


if __name__ == "__main__":
    # connnect to the MongoDB server on a localhost address
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs = client.logs
    nginx = logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    top_10_ips = nginx.aggregate([{
        "$group": {"_id": "$ip", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}}, {"$limit": 10}
        ])
    print("{} logs".format(nginx.estimated_document_count()))
    print("Methods:")
    for method in methods:
        print("\tmethod {}: {}".format(method,
            nginx.count_documents({"method": method}))
            )
    print("{} status check".format(nginx.count_documents({"method": "GET", "path": "/status"})))
    print("IPs:")
    for ip in top_10_ips:
        print("\t{}: {}".format(ip.get('_id'), ip.get('count')))
