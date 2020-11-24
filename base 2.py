from baseDB import Participante
from cantidadpart import cantidadpart
from ganadores import ganadores
from GuardarBD import GuardarBD
from puntomasalto import puntomasalto
from verpart import verpart
import sys
#pip install mysqlclient pymysql
#pip install sqlalchemy

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