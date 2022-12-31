from fastapi import FastAPI
from . import db
from cassandra.cqlengine.management import sync_table
from .models import User
# settings = get_settings()

app = FastAPI()


@app.on_event("startup")
def on_startup():
    db.session()
    sync_table(User)


@ app.get("/")
def root():
    return {"Hello": "world"}
