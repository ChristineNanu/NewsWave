from models import User, News, Category
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

app = FastAPI()
db_session = Session()

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

class NewsSchema(BaseModel):
    id: int
    description: str
    type: int
    category_id: int
    ads_id: int
    author_id: int

class CategorySchema(BaseModel):
    id: int
    name: str
    description: str
    type: int

class UpdateCategorySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[int] = None

    class Config:
        orm_mode = True

@app.get('/')
def hello():
    return "Hello"

@app.post('/add_user/{id}')
def post_user(user: UserSchema) -> UserSchema:
    new_user = User(**dict(user))
    db_session.add(new_user)
    db_session.commit()
    return user

@app.get('/news')
def get_news() -> list[News]:
    news = db_session.query(News).all()
    return news

@app.get('/category')
def get_category() -> list[Category]:
    category = db_session.query(Category).all()
    return category

@app.post('/add_category')
def post_category(category: CategorySchema) -> CategorySchema:
    new_category = Category(**dict(category))
    db_session.add(new_category)
    db_session.commit()
    return category

@app.patch('/category/partial-update/{id}')
def patch_category(id: int, payload: UpdateCategorySchema) -> CategorySchema:
    update_category = db_session.query(Category).filter_by(id=id).first()
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(update_category, key, value)
    db_session.commit()
    return update_category

@app.delete('/category/delete/{id}')
def delete_category(id: int) -> dict:
    deleted = db_session.query(Category).filter_by(id=id).first()
    db_session.delete(deleted)
    db_session.commit()
    return {"prompt": f"The category with id of {id} has been deleted."}
