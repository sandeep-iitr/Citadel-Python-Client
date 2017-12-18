#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

# importing the requests library
import requests
import json
from random import *

# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/data"


python_obj=dict()
python_obj['userToken']='eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MTA4MzY0ZS1iMWM4LTRmZDctOGU4Ni1mZDBlMTM4MDM5MDQifQ.N4SsfQP8thM_5DqEEPEER2AbQTYcGsPhr2HvuF4A7ho'
python_obj['uuid']='a397b5fe-098d-4b55-b16d-76f483cf3b26'
python_obj['data']=[]

lat_min=30
lat_max=35

lng_min=30
lng_max=35

for x in range(0, 100):
 lat=uniform(lat_min, lat_max) 
 lng=uniform(lng_min, lng_max) 
 timestamp=1451606400000+(x*1000) #31536000 seconds per year #MIN TIME: 1451606400000  #MAX TIME: 1452211200000

 python_obj['data'].insert(0, {'coordinates': [[lat, lng]], 'timestamp': timestamp, 'value': 15, 'geometryType': 'point'})

#print(python_obj['data'])
json_data=json.dumps(python_obj)

#print(json_data)

data=json_data
# Sending Data
r = requests.post(url = API_ENDPOINT, data = data, verify=False)

print("Response is:%s"%r.text)


#query the data from the API
#API_ENDPOINT_QUERY = "https://citadel.westus.cloudapp.azure.com:8080/api/querydata"
API_ENDPOINT_QUERY = "https://localhost:8080/api/querydata"


query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MTA4MzY0ZS1iMWM4LTRmZDctOGU4Ni1mZDBlMTM4MDM5MDQifQ.N4SsfQP8thM_5DqEEPEER2AbQTYcGsPhr2HvuF4A7ho","uuid":"a397b5fe-098d-4b55-b16d-76f483cf3b26","query":{"lat_min":30,"lat_max":35,"lng_min":30,"lng_max":35,"timestamp_min":1451606400000,"timestamp_max":1463142400000}}'


r = requests.post(url = API_ENDPOINT_QUERY, data = query, verify=False)

pastebin_url = r.text
print("Response is:%s"%r.text)
