import requests
apiurl = "https://apiejemplos.azurewebsites.net/api/departamentos"
#PYTHON NOS PERMITE CREARNOS OBJETOS DIRECTAMENTE COMO 
#FORMATO JSON
departamento = { "idDepartamento": 978, "nombre": "PYTHON", "localidad": "GIJON" }
response = requests.post(apiurl, json=departamento)
#PINTAMOS LA RESPUESTA DEL SERVIDOR (200 ES CORRECTO)
print("Status: " + str(response.status_code))