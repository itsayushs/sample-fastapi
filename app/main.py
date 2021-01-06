from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"data": "Hey World! This is a sample fastAPI GET Response."}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    #  http://127.0.0.1/items/5?q=somequery
    return {"item_id": item_id, "q": q}
