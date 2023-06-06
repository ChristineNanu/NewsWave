from sqlalchemy import Column, String, Integer, Boolean, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///news.db')

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    type = Column(String(), nullable=False)
    category_id = Column(Integer, nullable=False)
    ads_id = Column(Integer, nullable=False)
    author_id = Column(Integer, nullable=False)


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    type = Column(String(), nullable=False)

class Ads(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String(), nullable=False)
    description = Column(String(), nullable=False)
    title = Column(String(), nullable=False)

class Journalist(Base):
    __tablename__ = 'journalists'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(), nullable=False)
    email = Column(String(), nullable=False)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    password = Column(String(), nullable=False)

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(), nullable=False)
    payment_method = Column(String(), nullable=False)
    user_id = Column(Integer, nullable=False)
    status = Column(Boolean, nullable=False)

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
