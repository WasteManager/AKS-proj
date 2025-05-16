from fastapi import FastAPI, Request
import requests

app = FastAPI()

PARSER_SERVICE = "http://parser:8001/parse"

@app.post("/logs")
async def receive_log(request: Request):
    log_data = await request.json()
    # Send log to parser
    requests.post(PARSER_SERVICE, json=log_data)
    return {"status": "log received"}
