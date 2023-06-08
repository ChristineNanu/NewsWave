from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Category, Ads, Journalist, News

# Set up the database connection
engine = create_engine('sqlite:///news.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create an instance of the Faker class
faker = Faker()

# Generate and insert fake data into the database
for _ in range(10):
    # Create a Category
    category = Category(
        name=faker.name(),
        description=faker.paragraph(),
        type=faker.word(),
        images=faker.image_url()
    )
    session.add(category)

    # Create an Ads
    ads = Ads(
        date=faker.date(),
        description=faker.paragraph(),
        title=faker.company(),
        images=faker.image_url()
    )
    session.add(ads)

    # Create a Journalist
    journalist = Journalist(
        author=faker.name(),
        email=faker.email(),
        images=faker.image_url()
    )
    session.add(journalist)

    # Create a News
    news = News(
        description=faker.paragraph(),
        type=faker.word(),
        category=category,
        ads=ads,
        journalist=journalist
    )
    session.add(news)

# Commit the changes to the database
session.commit()

# Close the session
session.close()
