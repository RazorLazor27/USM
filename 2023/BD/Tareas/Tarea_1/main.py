import pyodbc
nombre_server = "DESKTOP-BC8H7JT"

try:
    conexion = pyodbc.connect('DRIVER={SQL SERVER};SERVER='+nombre_server+';DATABASE=Tarea1;UID=Root;PWD=admin1234')
    print("Conexion lograda")
    cursor = conexion.cursor()
    ##cursor.execute("SELECT @@version;")
    #row = cursor.fetchone()
    #print(row)
    cursor.execute("SELECT * FROM productos")
    rows = cursor.fetchall()
    for row in rows:
        print(row)



except Exception as e:
    print(e)

finally:
    conexion.close()
    print("Conexion Finalizada")