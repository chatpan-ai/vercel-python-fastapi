
from datetime import datetime

from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello from FastAPI!"}

@app.post("/postbot/entry")
async def postbot(request_body: dict):

    dialog = request_body['dialog']
    subjectId = dialog['subjectId']
    sbId = dialog['sbId']
    
    q = dialog['question']
    
    
    today = datetime.today()
    formatted_date = today.strftime("%Y-%m-%d")
    
    content_list = [f"{formatted_date}\n{q}"]

    response_body = {
        "code": 200,
        "msg": "OK",
        "data": content_list,
        "materialExtraInfoList": []
    }
    return response_body



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)