import os
import pandas as pd
import pyodbc


nombre_server = "DESKTOP-BC8H7JT"
conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+nombre_server+';DATABASE=FutUsm;UID=Root;PWD=admin')
cursor = conexion.cursor()


def mostrar_campeones(cursor,conexion):
    try:
        cursor.execute("""
                        SELECT anio, campeon
                            FROM resumen_WC
                            GROUP BY anio, campeon
                            ORDER BY anio DESC
                       """)
        
        for linea in cursor.fetchall():        
            print("En el año " + str(linea[0]) + " fue campeon: " + linea[1])
        

    except Exception as e:
        print("Hubo un error al llamar a la base de datos",e)

    return

def mostrar_3lugar(cursor, conexion):
    try:
        cursor.execute("""
                        SELECT tercerlugar, COUNT(*) AS count
                        FROM resumen_WC
                        group by tercerlugar
                        order by count DESC;
                       
                        """)
        i = 0
        while i < 5:
            result = cursor.fetchone()
            print("El equipo N°" + str(i+1)+ " con mas terceros lugares es "+ result[0] + " con " + str(result[1]) + " bronces")
            i += 1

    except Exception as e:
        print("Hubo un error al acceder a la base de datos",e)


""" Funcion para mostrar EL PAIS que mas partidos ha ganado en relacion a empates y derrotas"""
def mas_ganadores(cursor, conexion):
    try: 
        cursor.execute("""
                       SELECT equipo, sum(partidos_jugados), sum(victorias), sum(empates), sum(derrotas)
                       FROM mundiales
                       group by equipo
                       order by sum(partidos_jugados) DESC;
                       
                       
                       """)
        
        result_aux = 0
        for linea in cursor.fetchall():
            #print(linea)
            result = round((1 - ((linea[1]-linea[2])/linea[1])) * 100,2)
            if (result > result_aux):
                result_aux = result
                final = linea
            #result = round(result, 2)
            #print(result)
        
        print("El pais que mayor porcentaje de victorias tiene es: " + final[0]+ ", con un porcentaje de victoria del " + str(result_aux) + "%")
    except Exception as e:
        print("Error al llegar a la base de datos",e)


def podio_mas_veces(cursor, conexion):
    try:
        cursor.execute("""
                        SELECT total, COUNT(*) as contador
                        FROM (
                            SELECT total = campeon from resumen_WC
                            union all
                            SELECT total = subcampeon from resumen_WC
                            union all
                            SELECT total = tercerlugar from resumen_WC
                        ) A
                       
                        group by total
                        order by contador DESC
                       """)
        
        print("El pais que mas podios ha conseguido es " + str(cursor.fetchone()[0]) + " con " + str(cursor.fetchone()[1]) + " podios")

        # for linea in cursor.fetchall():
        #     print(linea)



    except Exception as e:
        print("Error al llegar a la base de datos", e)



#Funcion debe retornar cuando ha sido host, cuantas vcees ha sido campeon, cuantas goles ha hecho en la competencia, cuantas victorias
def preguntar_pais(cursor,conexion, pais):
    try:
        cursor.execute(f""" select 
                                m.equipo,
                                (select COUNT(equipo) from mundiales where equipo like '{pais}'),
                                (select COUNT(campeon) from resumen_WC where campeon like '{pais}'),
                                (select COUNT(subcampeon) from resumen_WC where subcampeon like '{pais}'),
                                (select COUNT(tercerlugar) from resumen_WC where tercerlugar like '{pais}'),
                                (select COUNT(host) from resumen_WC where host like '{pais}'),
                                (select SUM(partidos_jugados)),
                                (select SUM(victorias)),
                                (select SUM(derrotas)),
                                (select SUM(empates)),
                                (select SUM(goles_favor)),
                                (select SUM(goles_contra)),
                                (select SUM(puntos))

                            from 
                                mundiales m
                            where 
                                m.equipo like '{pais}'
                            group by 
                                m.equipo
                       
                       """)

        
        linea = cursor.fetchone()
        print(f"El equipo seleccionado fue: {linea[0]}, el cual ha aparecido {linea[1]} veces y ha logrado salir campeon {linea[2]} veces, tambien ha obtenido {linea[3]} 2dos lugares y {linea[4]} 3ros lugares, ademas ha sido el host de la copa {linea[5]} vez.")
        print(f"A nivel historico {linea[0]} ha jugado {linea[6]} partidos, donde consiguio: {linea[7]} victorias, {linea[8]} derrotas, {linea[9]} empates, {linea[10]} goles a favor y {linea[11]} en contra. Sumando asi {linea[12]} puntos")

    except Exception as e:
        print("Hubo un error al tratar de llegar a la base de datos" , e)
    return 


#Mostrar_goleadores(cursor, conexion)

# mostrar_campeones(cursor, conexion)
# mostrar_3lugar(cursor,conexion)
# mas_ganadores(cursor, conexion)
# podio_mas_veces(cursor, conexion)

preguntar_pais(cursor, conexion, "Uruguay")

cursor.close()
conexion.close()