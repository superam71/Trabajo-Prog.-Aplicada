import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine,desc,select,func,funcfilter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from baseDB import Participante,Base
import MySQLdb

class verpart:
    def __init__(self):
        engine=create_engine('sqlite:///participantes.db')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        stmt=session.query(Participante).order_by(Participante.edad).all()
        for item in stmt:
            print("Nombre: {} Edad: {} Puntaje: {}".format(item.nombre, item.edad, item.promediodisp))