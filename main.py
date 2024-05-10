from fastapi import FastAPI

from post import Post

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/posts")
async def posts():
    return Post(1, "title", "content")