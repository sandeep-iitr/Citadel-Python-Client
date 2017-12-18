#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8089/api/registerPolicy"

#Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","policy":{"sensors":["ee548c8c-5636-452d-b0a7-57fb4b6abeef"], "users":["testcitadel1@gmail.com","testcitadel3@gmail.com"]}}'

# Sending Data
#r = requests.post(url = API_ENDPOINT, data = Policy,verify=False)
#print("Response is:%s"%r.text)

#Spatio-Temporal Policy
#Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","policy":{"sensors":["ee548c8c-5636-452d-b0a7-57fb4b6abeef"], "users":["testcitadel1@gmail.com"], "where":{"allowedPolygons":[[{"lat":30.0,"lng":60.0},{"lat":40.0,"lng":60.0},{"lat":40.0,"lng":70.0},{"lat":30.0,"lng":70.0},{"lat":30.0,"lng":60.0}],[{"lat":30.0,"lng":60.0},{"lat":40.0,"lng":60.0},{"lat":40.0,"lng":70.0},{"lat":30.0,"lng":70.0},{"lat":30.0,"lng":60.0}]]}}}'

Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","policy":{"sensors":["ee548c8c-5636-452d-b0a7-57fb4b6abeef"], "users":["testcitadel1@gmail.com"], "where":{"allowedPolygons":[[{"lat":30.0,"lng":60.0},{"lat":40.0,"lng":60.0},{"lat":40.0,"lng":70.0},{"lat":30.0,"lng":70.0},{"lat":30.0,"lng":60.0}],[{"lat":5.0,"lng":5.0},{"lat":50.0,"lng":5.0},{"lat":50.0,"lng":70.0},{"lat":5.0,"lng":70.0},{"lat":5.0,"lng":5.0}]], "denyPolygons":[[{"lat":5.0,"lng":5.0},{"lat":10.0,"lng":5.0},{"lat":10.0,"lng":10.0},{"lat":5.0,"lng":10.0},{"lat":5.0,"lng":5.0}]]}}}'

r = requests.post(url = API_ENDPOINT, data = Policy,verify=False)
print("Response is:%s"%r.text)
