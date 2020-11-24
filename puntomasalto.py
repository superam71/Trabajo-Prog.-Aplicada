from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine,func
from sqlalchemy.orm import relationship,sessionmaker
from baseDB import Participante,Base
import MySQLdb

class puntomasalto:
    def __init__(self):
        engine=create_engine('sqlite:///participantes.db')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        minimo = session.query(func.min(Participante.promediodisp)).scalar()
        stmt=session.query(Participante).order_by(Participante.edad).all()
        for item in stmt:
            if item.promediodisp==minimo:
                print("Nombre: {} Puntaje: {}".format(item.nombre,item.promediodisp))