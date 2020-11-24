import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine,desc,select,func,funcfilter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from baseDB import Participante,Base
import MySQLdb

class cantidadpart:
    def __init__(self):
        engine=create_engine('sqlite:///participantes.db')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        cant=session.query(Participante.id).count()
        print("Cantidad de participantes: {}".format(cant))