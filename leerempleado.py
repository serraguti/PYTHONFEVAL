import requests
apiurl = "https://apiejemplos.azurewebsites.net/api/empleados/7839"
#SE REALIZA UNA PETICION Y SE CAPTURA UNA RESPUESTA
response = requests.get(apiurl)
#EN PYTHON EXISTE UN OBJETO QUE SE LLAMA DICCIONARIO
#DICHO OBJETO CONTIENE TODAS LAS PROPIEDADES MEDIANTE CORCHETES
#objeto["PROPIEDAD"]
#CUANDO LEEMOS UN OBJETO JSON, PODEMOS CONVERTIRLO A DICCIONARIO
empleado = response.json()
print(empleado)
print(empleado["apellido"])