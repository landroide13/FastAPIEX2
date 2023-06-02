from fastapi import FastAPI
from routes.user import user


app = FastAPI(
    title="Users REST API",
    description="version 0.0.0.1"
)

app.include_router(user)


















