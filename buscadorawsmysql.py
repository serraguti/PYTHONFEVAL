import mysql.connector

#ESTO SON COMENTARIOS
#DEBEMOS TENER CUIDADO CON LA TABULACION
#ES SUPER IMPORTANTE
print("Buscador AWS Mysql")

#DECLARAMOS UNA VARIABLE PARA LA CONEXION A MYSQL
#CON NUESTROS DATOS DE SERVER, USUARIO, PASSWORD Y BBDD
miConexion = mysql.connector.connect(
    host = "awsmysqlpaco.cf5cqucmwlm6.us-east-1.rds.amazonaws.com",
    user = "adminsql", 
    password = "Admin123", 
    database = "ejemplo"
)

#PEDIMOS UN DATO AL USUARIO, EL ID DEL COMIC A BUSCAR
print("Introduzca ID del Comic")
idcomic = input()
#CREAMOS LA CONSULTA CON UN WHERE PARA BUSCAR POR ID
sql = "select * from COMICS where IDCOMIC=" + idcomic
#CREAMOS UN CURSOR
cursor = miConexion.cursor()
#EJECUTAMOS LA CONSULTA
cursor.execute(sql)
#RECUPERO UNA FILA
fila = cursor.fetchone()
#PREGUNTAR SI EXISTE ALGUN REGISTRO
if (not fila):
    print("No hay registros")
else:
    print(fila)
#CERRAMOS LAS CONEXIONES
cursor.close()
miConexion.close()