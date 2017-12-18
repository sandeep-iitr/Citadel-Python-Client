# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://citadel.westus.cloudapp.azure.com:8080/api/registerSensor"

sensor = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkYmI2YWQ0My0yZDA2LTQ3OWEtOGE1Yy05NDJkZjM3YThjODgifQ.x-9hwjTm8JQ7tsqRTSb0G_qn1CWA9xZKhCYefdMvBHc","sensor":{"sensorType":"temperature","unit":"F"}}'


# Sending Data
r = requests.post(url = API_ENDPOINT, data = sensor,verify=False)

print("Response is:%s"%r.text)
