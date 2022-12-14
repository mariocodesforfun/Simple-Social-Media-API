from fastapi import Body, FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy import ForeignKey
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db
from .. import schemas, database, oath2 


router = APIRouter(
    prefix="/vote",
    tags=["Vote"]

)



@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int = Depends(oath2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == vote.post_id)

    post = db.query(models.Post).filter(models.Post.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post with id {vote.post_id} does not exist ")


    if not post_query.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, 
                            detail = f"Post with id {vote.post_id} was not found")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)

    if (vote.dir == 1):
        if vote_query.first():
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, 
                                detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "Successfully voted"}
    else:
        if not vote_query.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message": "Vote deleted successfully"}