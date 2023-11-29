import requests
apilambda = "https://383ukjunyh.execute-api.us-east-1.amazonaws.com/my-lambda-function-python"
response = requests.get(apilambda)
print(response)