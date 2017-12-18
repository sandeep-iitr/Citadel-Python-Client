#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/registerSensor"

sensor = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OGUyZDk3Yy0yYjBlLTRjZmUtYTIzOC1jMzEyMjFmZTIwYWMifQ.IR2yHOcOXkiMaCWFduOLjKxGLRkHhRJj_hsiand1CgQ","sensor":{"sensorType":"Sensor-1","unit":"Unit-1"}}'


# Sending Data
r = requests.post(url = API_ENDPOINT, data = sensor,verify=False)

print("Response is:%s"%r.text)
#The pastebin URL is:{"result":"SUCCESS","uuid":"e617d1a1-6323-4d5d-b66a-a63ab70ca349"}

#querying the Sensor just inserted.

API_ENDPOINT_QUERY = "https://localhost:8080/api/getSensor"


Sensor = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkMzBiMGEwMi1lOGE0LTRlYWItYjc5Ny1kODZhMDQ4OWU0ZDYifQ.Wig5mpzggNSxtehnSgOyAxXMzOGV-O6j5QrthipQvUg","uuid":"c2758131-bab9-40db-b295-421eae1ca8bf"}';

# Sending query
#r = requests.post(url = API_ENDPOINT_QUERY, data = Sensor,verify=False)

#print("Response is:%s"%r.text)



API_ENDPOINT_QUERY = "https://localhost:8080/api/querySensor"


Sensor = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkMzBiMGEwMi1lOGE0LTRlYWItYjc5Ny1kODZhMDQ4OWU0ZDYifQ.Wig5mpzggNSxtehnSgOyAxXMzOGV-O6j5QrthipQvUg","query":{"uuid":"c2758131-bab9-40db-b295-421eae1ca8bf"}}';

# Sending query
#r = requests.post(url = API_ENDPOINT_QUERY, data = Sensor,verify=False)

#print("Response is:%s"%r.text)
