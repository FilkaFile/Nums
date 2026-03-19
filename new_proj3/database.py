
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.sb'

engine = create_engine(SQALCHEMY_DATABASE_URL, connect_args={
                       'check_same_thread': False})


class Base(DeclarativeBase):
    pass


SessionLocal = sessionmaker(autoflush=False, bind=engine)
