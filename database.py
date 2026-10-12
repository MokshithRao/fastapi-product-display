from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

DATABASE_URL = "mysql+mysqlconnector://test:123456@localhost:3306/product_db"

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(bind=engine)

LocalSession = sessionmaker(bind=engine)

