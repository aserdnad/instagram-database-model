import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Name = Column(String(250), nullable=False)
    Password = Column(String(15), nullable=False)
    Email = Column(String(30), nullable=False)

class Perfil(Base):
    __tablename__ = 'Perfil'
    # Here we define columns for the table Profile.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('Usuario.id'))
    Name = Column(String(250), nullable=False)
    Bio = Column(String(250))
    UrlImagen = Column(String(250))
    Followers = Column(Integer)
    Followed = Column(Integer)
    usuario = relationship(Usuario)

class Publicacion(Base):
    __tablename__ = 'Publicacion'
    id = Column(Integer, primary_key=True)
    Perfil_id = Column(Integer, ForeignKey('Perfil.id'))
    Hora = Column(DateTime,nullable=False)
    Location = Column(String(250))
    Url_imagen = Column(String(250))
    perfil = relationship(Perfil)

class Comentarios(Base):
    __tablename__ = 'Comentarios'
    id = Column(Integer, primary_key=True)
    Publicacion_id = Column(Integer, ForeignKey('Publicacion.id'))
    Perfil_id = Column(Integer, ForeignKey('Perfil.id'))
    Texto = Column(String(250),nullable=False)
    perfil = relationship(Perfil)
    publicacion = relationship(Publicacion)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e