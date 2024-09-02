from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///main.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()
