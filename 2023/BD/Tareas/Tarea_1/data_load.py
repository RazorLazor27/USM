import os
import pandas as pd
import pyodbc




directorio = os.path.dirname(os.path.abspath(__file__))
subcarpeta = os.path.join(directorio, "src")

#Archivos_aux una lista con todos los archivos csv, lesgo
archivos_aux = [file for file in os.listdir(subcarpeta) if os.path.isfile(os.path.join(subcarpeta, file))]
archivos_aux.pop()


def new_database(cadena):
    con = pyodbc.connect(cadena)
    con.autocommit = True
    cursor = con.cursor()
    cursor.execute("SELECT database_id FROM sys.databases WHERE Name = 'FutUsm'")
    flag = cursor.fetchone()

    if not flag:
        cursor.execute("CREATE DATABASE FutUsm")
        print("===La base de datos FutUsm ha sido creada.===")
    
    cursor.close()
    con.close()
    return

def tabla_datadeanios(cursor, connec):
    cursor.execute("""
        CREATE TABLE mundiales(
            id INT IDENTITY(1,1) PRIMARY KEY NOT NULL,
            posicion INT,
            equipo VARCHAR(100),
            partidos_jugados INT,
            victorias INT,
            empates INT,
            derrotas INT,
            goles_favor INT,
            goles_contra INT,
            goles_diff NVARCHAR(10),
            puntos INT
            )
                   
                   """)
    
    query = "INSERT INTO mundiales (posicion, equipo, partidos_jugados, victorias, empates, derrotas, goles_favor, goles_contra, goles_diff, puntos) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
  

    for entrada in archivos_aux:
        dataframe = pd.read_csv('src/'+entrada, skiprows=1, names = ['posicion','equipo','partidos_jugados','victorias','empates','derrotas','goles_favor','goles_contra','goles_diff','puntos'])

        for index, row in dataframe.iterrows():
            cursor.execute(query, (row['posicion'], row['equipo'], row['partidos_jugados'], row['victorias'], row['empates'], row['derrotas'], row['goles_favor'], row['goles_contra'], row['goles_diff'], row['puntos']))

    connec.commit()
    print("Parece que algo funciono")
    
    return

def tabla_resumen_WC(cursor, connec):
    cursor.execute("""
        CREATE TABLE resumen_WC(
            anio INT PRIMARY KEY,
            host NVARCHAR(30),
            campeon NVARCHAR(30),
            subcampeon NVARCHAR(30),
            tercerlugar NVARCHAR(30),
            cant_equipos INT,
            partidos_jugados INT,
            goles_totales INT,
            gpp FLOAT
            )
                   
                   """)
    
    dataframe = pd.read_csv("src/FIFA - World Cup Summary.csv", skiprows=1, names= ['anio','host','campeon','subcampeon','tercerlugar','cant_equipos','partidos_jugados','goles_totales','gpp'])
    
    query = "INSERT INTO resumen_WC (anio, host, campeon, subcampeon, tercerlugar, cant_equipos, partidos_jugados, goles_totales, gpp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    
    for index, row in dataframe.iterrows(): #El index aqui hace que la cosa no explote
        cursor.execute(query, (row['anio'], row['host'], row['campeon'], row['subcampeon'], row['tercerlugar'], row['cant_equipos'], row['partidos_jugados'], row['goles_totales'], row['gpp']))
    
    connec.commit()
    print("otra tabla creo")
    
    return    



nombre_server = "DESKTOP-BC8H7JT" #FLAN cambia esto al nombre de servidor 
new_database('DRIVER={SQL SERVER};SERVER='+nombre_server+';DATABASE=master;UID=Root;PWD=admin')


conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+nombre_server+';DATABASE=FutUsm;UID=Root;PWD=admin')
cursor = conexion.cursor()


tabla_datadeanios(cursor, conexion)
tabla_resumen_WC(cursor, conexion)


cursor.close()
conexion.close()

