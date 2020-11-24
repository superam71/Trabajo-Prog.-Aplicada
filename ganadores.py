import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine,desc,select,func,funcfilter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from baseDB import Participante,Base
import MySQLdb

class ganadores:
    def __init__(self):
        puestos=[1,2,3]
        engine=create_engine('sqlite:///participantes.db')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        stmt=session.query(Participante).order_by(Participante.promediodisp).limit(3) #3 primeros en la base ordenada
        for item in stmt:
            print("Puesto {} Nombre: {} Puntaje: {}".format(puestos[0],item.nombre,item.promediodisp))
            puestos.pop(0)