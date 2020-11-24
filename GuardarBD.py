import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine,desc,select,func,funcfilter
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from baseDB import Participante,Base
import MySQLdb

def GuardarBD():
    engine=create_engine('sqlite:///participantes.db')
    Base.metadata.bind=engine
    DBSession=sessionmaker(bind=engine)
    session=DBSession()
    nombre=input("ingrese su nombre\n")
    apellido=input("ingrese su apellido\n")
    edad=int(input("ingrese su edad\n"))
    sexo=input("ingrese su sexo. M/F\n")
    ubicaciondisp1=float(input("ingrese la coordenada del primer disparo(x.y)\n"))
    ubicaciondisp2=float(input("ingrese la coordenada del segundo disparo(x.y)\n"))
    ubicaciondisp3=float(input("ingrese la coordenada del tercer disparo(x.y)\n"))
    promedio=ubicaciondisp1+ubicaciondisp2+ubicaciondisp3/3
    promediodisp="{0:.2f}".format(promedio)

    print("Disparo n1: {} Disparo n2: {} Disparo n3: {} Promedio: {}".format(ubicaciondisp1,ubicaciondisp2,ubicaciondisp3,promediodisp))

    user=Participante(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        sexo=sexo,
        ubicaciondisp1=ubicaciondisp1,
        ubicaciondisp2=ubicaciondisp2,
        ubicaciondisp3=ubicaciondisp3,
        promediodisp=promediodisp
        )

    session.add(user) #Agregar sesion

    session.commit() #Guardar

    session.close() #Cerrar sesion