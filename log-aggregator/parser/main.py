from fastapi import FastAPI, Request
from pymongo import MongoClient
import datetime

app = FastAPI()

client = MongoClient("mongodb://mongodb:27017/")
db = client["logs"]
collection = db["entries"]

@app.post("/parse")
async def parse_log(request: Request):
    data = await request.json()
    parsed = {
        "timestamp": datetime.datetime.utcnow().isoformat(),
        "level": data.get("level", "INFO"),
        "message": data.get("message", ""),
        "source": data.get("source", "unknown")
    }
    collection.insert_one(parsed)
    return {"status": "parsed and stored"}
