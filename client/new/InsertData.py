# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://citadel.westus.cloudapp.azure.com:8080/api/data"

# data to be sent to api
data = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","uuid":"ee548c8c-5636-452d-b0a7-57fb4b6abeef","data":[{"timestamp":1499813708623,"value":15,"geometryType":"point","coordinates":[[10,10]]}]}'

# Sending Data
r = requests.post(url = API_ENDPOINT, data = data, verify=False)
print("Response is:%s"%r.text)

