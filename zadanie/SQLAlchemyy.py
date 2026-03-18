from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQALCHEMY_DATABASE_URL = 'sqlite:///./sql_app.sb'

engine = create_engine(SQALCHEMY_DATABASE_URL, connect_args={
                       'check_same_thread': False})


class Base(DeclarativeBase):
    pass


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    price = Column(Float)
    stock = Column(Integer)


Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autoflush=False, bind=engine)
