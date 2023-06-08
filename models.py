from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, backref

Base = declarative_base()
engine = create_engine('sqlite:///news.db')

class News(Base):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    description = Column(String())
    type = Column(String())
    category_id = Column(Integer, ForeignKey('categories.id'))
    ads_id = Column(Integer,  ForeignKey('ads.id'))
    author_id = Column(Integer, ForeignKey('journalists.id'))
    


class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    description = Column(String())
    type = Column(String())
    images = Column(String())
    news = relationship('News', backref=backref('category'))

class Ads(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    date = Column(String())
    description = Column(String())
    title = Column(String())
    images = Column(String())
    news = relationship('News', backref=backref('ads'))

class Journalist(Base):
    __tablename__ = 'journalists'

    id = Column(Integer, primary_key=True)
    author = Column(String())
    email = Column(String())
    images = Column(String())
    news = relationship('News', backref=backref('journalist'))

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(), nullable=False)
    email = Column(String(), nullable=False)
    password = Column(String(), nullable=False)
    subscription= relationship('Subscription', backref=backref('user'))

class Subscription(Base):
    __tablename__ = 'subscriptions'

    id = Column(Integer, primary_key=True)
    type = Column(String())
    payment_method = Column(String())
    user_id = Column(Integer, ForeignKey('users.id'))
    status = Column(String(), nullable=False) 

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


