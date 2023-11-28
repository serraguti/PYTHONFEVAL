import requests
apiurl = "https://apiejemplos.azurewebsites.net/api/departamentos"
departamento = {"idDepartamento": 978, "nombre": "UPDATE", "localidad": "OVIEDO"}
response = requests.put(apiurl, json=departamento)
print("Status " + str(response.status_code))