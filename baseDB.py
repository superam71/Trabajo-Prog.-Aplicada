import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

Base = declarative_base()

class Participante(Base):#Participante
    __tablename__='participantes'
    id=Column(Integer, primary_key=True)
    nombre=Column(String(50), nullable=False)
    apellido=Column(String(50), nullable=False)
    edad=Column(Integer,nullable=False)
    sexo=Column(String(1), nullable=False)
    ubicaciondisp1=Column(Integer)
    ubicaciondisp2=Column(Integer)
    ubicaciondisp3=Column(Integer)
    promediodisp=Column(Float)

engine=create_engine('sqlite:///participantes.bd')
Base.metadata.create_all(engine)