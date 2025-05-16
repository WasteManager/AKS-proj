from fastapi import FastAPI, Query
from pymongo import MongoClient

app = FastAPI()

client = MongoClient("mongodb://mongodb:27017/")
db = client["logs"]
collection = db["entries"]

@app.get("/search")
def search_logs(level: str = None):
    query = {}
    if level:
        query["level"] = level
    results = list(collection.find(query, {"_id": 0}))
    return results
