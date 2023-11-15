import mysql.connector

#ESTO SON COMENTARIOS
#DEBEMOS TENER CUIDADO CON LA TABULACION
#ES SUPER IMPORTANTE
print("Eliminar MySQL AWS")

#DECLARAMOS UNA VARIABLE PARA LA CONEXION A MYSQL
#CON NUESTROS DATOS DE SERVER, USUARIO, PASSWORD Y BBDD
miConexion = mysql.connector.connect(
    host = "awsmysqlpaco.cf5cqucmwlm6.us-east-1.rds.amazonaws.com",
    user = "adminsql", 
    password = "Admin123", 
    database = "ejemplo"
)

cursor = miConexion.cursor()
#PEDIMOS EL ID A ELIMINAR
print("Introduzca el ID del Comic a eliminar")
idcomic = input()
#delete from COMICS where IDCOMIC=11
#ESCRIBIMOS LA CONSULTA CON EL PARAMETRO
sql = "delete from COMICS where IDCOMIC=" + idcomic
#EJECUTAMOS LA CONSULTA
cursor.execute(sql)
#DIBUJAMOS LOS REGISTROS AFECTADOS
print("Comics eliminados: " + str(cursor.rowcount))
#FINALIZAMOS LA TRANSACCION
miConexion.commit()
cursor.close()
miConexion.close()