import mysql.connector

#ESTO SON COMENTARIOS
#DEBEMOS TENER CUIDADO CON LA TABULACION
#ES SUPER IMPORTANTE
print("Modificar MySQL AWS")

#DECLARAMOS UNA VARIABLE PARA LA CONEXION A MYSQL
#CON NUESTROS DATOS DE SERVER, USUARIO, PASSWORD Y BBDD
miConexion = mysql.connector.connect(
    host = "awsmysqlpaco.cf5cqucmwlm6.us-east-1.rds.amazonaws.com",
    user = "adminsql", 
    password = "Admin123", 
    database = "ejemplo"
)

#DECLARAMOS UN CURSOR
cursor = miConexion.cursor()
#PEDIMOS DATOS AL USUARIO
print("Id Comic a modificar")
idcomic = input()
print("Nuevo nombre")
nombre = input()
print("Nueva imagen")
imagen = input()
print("Descripcion")
descripcion = input()
#REALIZAMOS LA CONSULTA LITERAL
sql = "update COMICS set NOMBRE='"+nombre+"', IMAGEN='"+imagen+"', DESCRIPCION='"+descripcion+"' where IDCOMIC=" + idcomic
#EJECUTAMOS LA CONSULTA
cursor.execute(sql)
#DIBUJAMOS LOS COMICS MODIFICADOS
print("Comics modificados: " + str(cursor.rowcount))
#EJECUTAMOS LA TRANSACCION
miConexion.commit()
cursor.close()
miConexion.close()

