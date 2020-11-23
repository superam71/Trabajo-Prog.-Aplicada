import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker
from sqlalchemy.pool import StaticPool
from baseDB import Participante,Base

def GuardarBD():#Guardardatos
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

    user=Participante(
        nombre=nombre,
        apellido=apellido,
        edad=edad,
        sexo=sexo,
        ubicaciondisp1=ubicaciondisp1,
        ubicaciondisp2=ubicaciondisp2,
        ubicaciondisp3=ubicaciondisp3,
        promediodisp=promediodisp)

    session.add(user) #Agregar

class verpart:
    def __init__(self):
        engine=create_engine('sqlite:///participantes.bd')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        resultados=session.query(Participante).all()

        for item in resultados:
            print("nombre: {} edad: {}".format(item.nombre, item.edad))

while True:
    #Crear participante
    pregunta=int(input("1:Ingresar participante,2.Ver participantes 3:Salir"))
    if pregunta==1:
        GuardarBD()
    elif pregunta==2:
        verpart()
    #Salir
    elif pregunta==3:
        sys.exit()