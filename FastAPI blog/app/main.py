from fastapi import FastAPI
from app.routers import users, posts

app = FastAPI()

# Include routers
app.include_router(users.router)
app.include_router(posts.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Blog!"}
