#IMPORTAMOS LA LIBRERIA DE MYSQL
import mysql.connector

#ESTO SON COMENTARIOS
#DEBEMOS TENER CUIDADO CON LA TABULACION
#ES SUPER IMPORTANTE
print("Mi primer Python")

#DECLARAMOS UNA VARIABLE PARA LA CONEXION A MYSQL
#CON NUESTROS DATOS DE SERVER, USUARIO, PASSWORD Y BBDD
miConexion = mysql.connector.connect(
    host = "awsmysqlpaco.cf5cqucmwlm6.us-east-1.rds.amazonaws.com",
    user = "adminsql", 
    password = "Admin123", 
    database = "ejemplo"
)

#VAMOS A LEER TODOS LOS COMICS Y CREAMOS UN CURSOS
miCursor = miConexion.cursor()
#NECESITAMOS UNA CONSULTA DE LOS DATOS
sql = "select * from COMICS"
#EJECUTAMOS LA CONSULTA CON EL CURSOR
miCursor.execute(sql)
#RECORREMOS TODOS LOS DATOS
for fila in miCursor:
    #SI NECESITAMOS PINTAR UNA COLUMNNA
    print(fila[1])
    #print(fila['NOMBRE'])

miCursor.close()
miConexion.close()