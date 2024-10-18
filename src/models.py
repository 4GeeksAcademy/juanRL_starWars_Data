import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)  
    email = Column(String(250), nullable=False)  
    password = Column(String(250), nullable=False)  
    firstname = Column(String(250), nullable=False)  
    lastname = Column(String(250), nullable=False)  
    subscription_date = Column(DateTime, default=datetime.utcnow)  
    
    favorites = relationship('Favorite', backref='user', lazy=True)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)  
    height = Column(String(250), nullable=True) 
    mass = Column(String(250), nullable=True)  
    hair_color = Column(String(250), nullable=True)  
    skin_color = Column(String(250), nullable=True)  
    eye_color = Column(String(250), nullable=True)  
    birth_year = Column(String(250), nullable=True)  
    gender = Column(String(250), nullable=True)  
    homeworld = Column(String(250), nullable=True)  
    
    favorites = relationship('Favorite', backref='character', lazy=True)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)  
    diameter = Column(String(250), nullable=True)  
    rotation_period = Column(String(250), nullable=True)  
    orbital_period = Column(String(250), nullable=True) 
    gravity = Column(String(250), nullable=True)  
    population = Column(String(250), nullable=True) 
    climate = Column(String(250), nullable=True)  
    terrain = Column(String(250), nullable=True)  
    
    favorites = relationship('Favorite', backref='planet', lazy=True)

class Starship(Base):
    __tablename__ = 'starship'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)  
    model = Column(String(250), nullable=True)  
    starship_class = Column(String(250), nullable=True)  
    manufacturer = Column(String(250), nullable=True) 
    cost_in_credits = Column(String(250), nullable=True)  
    length = Column(String(250), nullable=True) 
    crew = Column(String(250), nullable=True) 
    passengers = Column(String(250), nullable=True)  
    max_atmosphering_speed = Column(String(250), nullable=True) 
    hyperdrive_rating = Column(String(250), nullable=True)  
    MGLT = Column(String(250), nullable=True)  
    cargo_capacity = Column(String(250), nullable=True)  
    consumables = Column(String(250), nullable=True)  
    
    favorites = relationship('Favorite', backref='starship', lazy=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False) 
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)  
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True) 
    starship_id = Column(Integer, ForeignKey('starship.id'), nullable=True)  

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
