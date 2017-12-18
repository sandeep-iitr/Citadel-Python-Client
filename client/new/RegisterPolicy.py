
# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://citadel.westus.cloudapp.azure.com:8089/api/registerPolicy"

#Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","policy":{"sensors":["ee548c8c-5636-452d-b0a7-57fb4b6abeef"], "users":["testcitadel1@gmail.com","testcitadel3@gmail.com"]}}'

# Sending Data
#r = requests.post(url = API_ENDPOINT, data = Policy,verify=False)
#print("Response is:%s"%r.text)

#Spatio-Temporal Policy
#Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","policy":{"sensors":["ee548c8c-5636-452d-b0a7-57fb4b6abeef"], "users":["testcitadel1@gmail.com"], "where":{"allowedPolygons":[[{"lat":30.0,"lng":60.0},{"lat":40.0,"lng":60.0},{"lat":40.0,"lng":70.0},{"lat":30.0,"lng":70.0},{"lat":30.0,"lng":60.0}],[{"lat":30.0,"lng":60.0},{"lat":40.0,"lng":60.0},{"lat":40.0,"lng":70.0},{"lat":30.0,"lng":70.0},{"lat":30.0,"lng":60.0}]]}}}'

#Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkYmI2YWQ0My0yZDA2LTQ3OWEtOGE1Yy05NDJkZjM3YThjODgifQ.x-9hwjTm8JQ7tsqRTSb0G_qn1CWA9xZKhCYefdMvBHc","policy":{"sensors":["302ce0e0-80d4-4b0e-8c3e-c76fb756d4be"], "users":["testcitadel1@gmail.com"], "where":{"allowedPolygons":[[{"lat":32.0,"lng":62.0},{"lat":33.0,"lng":62.0},{"lat":33.0,"lng":63.0},{"lat":32.0,"lng":63.0},{"lat":32.0,"lng":62.0}]], "denyPolygons":[[{"lat":5.0,"lng":5.0},{"lat":10.0,"lng":5.0},{"lat":10.0,"lng":10.0},{"lat":5.0,"lng":10.0},{"lat":5.0,"lng":5.0}]]}}}'

Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkYmI2YWQ0My0yZDA2LTQ3OWEtOGE1Yy05NDJkZjM3YThjODgifQ.x-9hwjTm8JQ7tsqRTSb0G_qn1CWA9xZKhCYefdMvBHc","policy":{"sensors":["302ce0e0-80d4-4b0e-8c3e-c76fb756d4be"], "users":["testcitadel1@gmail.com"]}}'


r = requests.post(url = API_ENDPOINT, data = Policy,verify=False)
print("Response is:%s"%r.text)
