from datetime import datetime
import imp
from lib2to3.pgen2 import token
from logging import raiseExceptions

from os import access
from tokenize import Token
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from .. import database
from sqlalchemy.orm import Session 
from .. import models, utils, oath2 
from .. import schemas
from fastapi.security import OAuth2PasswordBearer




router = APIRouter(tags=['Authentication'])





@router.post("/login", response_model=schemas.Token)
def login(user_credentials: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.username).first()

    if not user:
        raise HTTPException(status.HTTP_403_FORBIDDEN, 
                            detail="Invalid credentials")
    

    if not utils.verify(user_credentials.password, user.password):
        raise HTTPException(status.HTTP_403_FORBIDDEN, detail="Invalid credentials")

    access_token = oath2.create_token(data = {"user_id": user.id})

    return {"access_token": access_token, "token_type": "bearer"}


    
