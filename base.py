import sys
import datetime
from sqlalchemy import Column,ForeignKey,Integer,String,DateTime,Float,create_engine,engine,desc,select,func
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

class verpart:
    def __init__(self):
        engine=create_engine('sqlite:///participantes.db')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        stmt=session.query(Participante).order_by(Participante.edad).all()
        for item in stmt:
            print("Nombre: {} Edad: {}".format(item.nombre, item.edad))

class cantidadpart:
    def __init__(self):
        engine=create_engine('sqlite:///participantes.db')
        Base.metadata.bind=engine
        DBSession=sessionmaker(bind=engine)
        session=DBSession()
        cant=session.query(Participante.id).count()
        print("Cantidad de participantes: {}".format(cant))

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

while True:
    pregunta=int(input("1:Ingresar participante,2:Ver participantes,3:Cantidad de participantes,4:Punto mas alto,5:Ganadores,6:Salir"))
    #Crear participante
    if pregunta==1:
        GuardarBD()
    #Ver Partcipantes
    elif pregunta==2:
        verpart()
    #Cantidad de participantes
    elif pregunta==3:
        cantidadpart()
    #Punto mas alto
    elif pregunta==4:
        puntomasalto()
    #Ganadores
    elif pregunta==5:
        ganadores()
    #Salir
    elif pregunta==6:
        sys.exit(0)