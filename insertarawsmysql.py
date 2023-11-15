import mysql.connector

#ESTO SON COMENTARIOS
#DEBEMOS TENER CUIDADO CON LA TABULACION
#ES SUPER IMPORTANTE
print("Insertar MySQL AWS")

#DECLARAMOS UNA VARIABLE PARA LA CONEXION A MYSQL
#CON NUESTROS DATOS DE SERVER, USUARIO, PASSWORD Y BBDD
miConexion = mysql.connector.connect(
    host = "awsmysqlpaco.cf5cqucmwlm6.us-east-1.rds.amazonaws.com",
    user = "adminsql", 
    password = "Admin123", 
    database = "ejemplo"
)

#PARA LAS CONSULTAS DE ACCION TAMBIEN SE UTILIZA Ç
#UN CURSOR PARA LA EJECUCION, SOLO QUE NO DEVUELVE DATOS
cursor = miConexion.cursor()
#PEDIMOS DATOS PARA EL NUEVO COMIC
print("Id Comic")
idcomic = input()
print("Titulo del Comic")
nombre = input()
print("Imagen del comic")
imagen = input()
print("Descripción")
descripcion = input()
#DEBEMOS TENER CUIDADO CON LAS COMILLAS SIMPLES CUANDO SEAN STRING
#LO MEJOR ES ESCRIBIR LA CONSULTA Y SUSTITUIR
sql = "insert into COMICS values (" + idcomic + ", '" + nombre + "', '" + imagen + "', '" + descripcion + "')"
#EJECUTAMOS LA CONSULTA SQL
cursor.execute(sql)
#AL SER UN CURSOR DE CONSULTA DE ACCION TIENE UNA PROPIEDAD
#PARA SABER EL NUMERO DE REGISTROS QUE HA EJECUTADO
print("Insertados: " + str(cursor.rowcount))
#CON LAS CONSULTAS DE ACCION DEBEMOS CERRAR LA TRANSACCION
miConexion.commit()
cursor.close()
miConexion.close()