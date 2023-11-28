import requests
apiurl = "https://apiejemplos.azurewebsites.net/api/departamentos/978"
response = requests.delete(apiurl)
print("Status: " + str(response.status_code))