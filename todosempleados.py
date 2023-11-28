import requests
apiurl = "https://apiejemplos.azurewebsites.net/api/empleados"
response = requests.get(apiurl)
#LA UNICA DIFERENCIA ESTA EN QUE NOS DEVOLVERA
#UN CONJUNTO DE ELEMENTOS DICCIONARIO
empleados = response.json()
print("Lista de empleados")
for emp in empleados:
    print(emp["apellido"] + ", Oficio: " + emp["oficio"])