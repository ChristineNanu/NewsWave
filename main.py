from models import User, News, Category, Subscription, Journalist
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List
from models import Session

db_session = Session()
app = FastAPI()

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
    type: str

    class Config:
        orm_mode = True

class SubscriptionSchema(BaseModel):
    id: int
    type: str
    payment_method: str

    class Config:
        orm_mode = True

class JournalistSchema(BaseModel):
    id: int
    author: str
    email: str
    images: str

    class Config:
        orm_mode = True

class CategorySchema(BaseModel):
    id: int
    name: str
    description: str
    type: str
    images: str

    class Config:
        orm_mode = True

class UpdateCategorySchema(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    description: Optional[str] = None
    type: Optional[str] = None
    images: Optional[str] = None

    class Config:
        orm_mode = True

@app.get('/')
def hello():
    return "Hello"

@app.post('/add_user')
def post_user(user: UserSchema) -> UserSchema:
    new_user = User(**dict(user))
    db_session.add(new_user)
    db_session.commit()
    return user

@app.get('/news')
def get_news():
    news = db_session.query(News).all()
    return news

@app.get('/all_categories')
def get_all_categories():
    categories = db_session.query(Category).all()
    return categories

@app.get('/categories')
def get_categories_according_to_type(type: str):
    categories = db_session.query(Category).filter_by(type=type)
    return categories

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

@app.post('/add_subscription/{id}')
def post_user(sub: SubscriptionSchema) -> SubscriptionSchema:
    new_sub = Subscription(**dict(sub))
    db_session.add(new_sub)
    db_session.commit()
    return sub

@app.post('/add_journalist/{id}')
def post_journalist(journalist: JournalistSchema) -> JournalistSchema:
    new_journalist = Journalist(**dict(journalist))
    db_session.add(new_journalist)
    db_session.commit()
    return journalist

@app.get('/all_journalists')
def get_all_journalists()-> List[JournalistSchema]:
   journalists = db_session.query(Journalist).all()
   return journalists

@app.get('/journalist/{id}')
def get_journalist(id: int):
   journalist = db_session.query(Journalist).filter_by(id=id).first()
   return journalist