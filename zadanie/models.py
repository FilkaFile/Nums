from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    employees = relationship('Person', back_populates='company')


class Product(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)
    company_id = Column(Integer, ForeignKey('companies.id'))

    company = relationship('Company', back_populates='employees')
