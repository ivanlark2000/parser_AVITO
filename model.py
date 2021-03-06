import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, TIMESTAMP, VARCHAR, ForeignKey, Text, Numeric, Boolean
from sqlalchemy.orm import relation
from dotenv import load_dotenv


load_dotenv(override=True)
USERNAME_DB = os.environ.get('user_DB')
PASSWORD_DB = os.environ.get('password_DB')

engine = create_engine(f'postgresql://{USERNAME_DB}:{PASSWORD_DB}@localhost/flats', echo=False)
Base = declarative_base()


class Flat(Base):
    __tablename__ = "flat"

    id = Column(Integer, primary_key=True)
    id_avito = Column(Integer)
    number = Column(Integer)
    price = Column(Numeric(15, 2), nullable=False)
    qty_of_rooms = Column(Integer)
    total_space = Column(Numeric(3, 2), nullable=False)
    square_of_kitchen = Column(Numeric(3, 2), nullable=False)
    living_space = Column(Numeric(3, 2), nullable=False)
    floor = Column(Integer, nullable=False)
    furniture = Column(String(200))
    technics = Column(String(200))
    balcony_or_loggia = Column(Boolean, nullable=False)
    room_type = Column(String(120))
    ceiling_height = Column(Numeric(3, 2))
    bathroom = Column(String(120))
    widow = Column(String(120))
    repair = Column(String(120))
    seilling_method = Column(String(120))
    transaction_type = Column(String(120))
    decorating = Column(String(120))
    district_id = Column(Integer, ForeignKey('district.id'), nullable=False)
    house_id = Column(Integer, ForeignKey('house.id'), nullable=False)


class House(Base):
    __tablename__ = 'house'

    id = Column(Integer, primary_key=True)
    area = Column(String(150))
    street = Column(String(200), nullable=False)
    number_of_house = Column(Integer)
    new_building_name = Column(String(200))
    offical_builder = Column(String(200))
    year_of_construction = Column(Integer)
    floors_in_the_hourse = Column(Integer)
    passenger_bodice = Column(Boolean, nullable=False)
    service_lift = Column(Boolean, nullable=False)
    in_home = Column(String(200))
    pemolition_planned = Column(String(200))
    type_of_bilding = Column(String(200))
    yard = Column(String(200))
    parking = Column(String(200))
    deadline = Column(String(150))
    district_id = Column(Integer, ForeignKey('district.id'), nullable=False)


class District(Base):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True)
    name_area = Column(String(255), nullable=True)
