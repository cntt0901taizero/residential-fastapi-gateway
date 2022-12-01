from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src import database_fastapi, token
from src.models import fastapi_models
from src.hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(
    tags=['Authentication FastAPI']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database_fastapi.get_db)):
    user = db.query(fastapi_models.User).filter(
        fastapi_models.User.email == request.username or fastapi_models.User.name == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Invalid Credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Incorrect password")

    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
