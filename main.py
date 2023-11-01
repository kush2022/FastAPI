from fastapi import FastAPI, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from blog import schemas, models
from blog.database import engine, get_db
from typing import List
from blog.hashing import Hash
from blog.routers import blog, user, authentication


app = FastAPI()

app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)



models.Base.metadata.create_all(engine)



# -- create user 
