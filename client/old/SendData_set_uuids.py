#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/data"

# data to be sent to api
#data = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MTA4MzY0ZS1iMWM4LTRmZDctOGU4Ni1mZDBlMTM4MDM5MDQifQ.N4SsfQP8thM_5DqEEPEER2AbQTYcGsPhr2HvuF4A7ho","uuid":"a397b5fe-098d-4b55-b16d-76f483cf3b26","data":[{"timestamp":10000000,"value":15,"geometryType":"point","coordinates":[[-30,-160]]}]}'
data = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MTA4MzY0ZS1iMWM4LTRmZDctOGU4Ni1mZDBlMTM4MDM5MDQifQ.N4SsfQP8thM_5DqEEPEER2AbQTYcGsPhr2HvuF4A7ho","uuid":"a397b5fe-098d-4b55-b16d-76f483cf3b26","data":[{"timestamp":1451606500000,"value":15,"geometryType":"point","coordinates":[[31,61]]}]}'


# Sending Data
r = requests.post(url = API_ENDPOINT, data = data, verify=False)

print("Response is:%s"%r.text)


#query the data from the API
#API_ENDPOINT_QUERY = "https://citadel.westus.cloudapp.azure.com:8080/api/querydata"
API_ENDPOINT_QUERY = "https://localhost:8080/api/querydata"

#query to be send to api
#query="{\"userToken\":\"9d1b5507-fc17-47c9-9517-6b8f4f3e5f28\",\"uuid\":\"bacfa2ba-df15-4d1c-9575-d32c47ed24a1\",\"query\":{\"lat_min\":29,\"lat_max\":31,\"lng_min\":59,\"lng_max\":61,\"timestamp_min\":1499813608623,\"timestamp_max\":1499813808623}}"

#query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","uuid":"ee548c8c-5636-452d-b0a7-57fb4b6abeef","query":{"lat_min":29,"lat_max":31,"lng_min":59,"lng_max":61,"timestamp_min":1499813608623,"timestamp_max":1499813808623}}'

#query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","uuid":"ee548c8c-5636-452d-b0a7-57fb4b6abeef","query":{"lng_min":20,"lng_max":60,"lat_min":20,"lat_max":60,"timestamp_min":1453951873000,"timestamp_max":1453973873000}}'
#query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzMmNiOTljYS1lMTRkLTQ1OGMtOTAwOS00MjI4NGMwMTk4YTIifQ.DpPJ0nuh4EvAdEG28nWcwMkjMZ7KIlPLtQu1idRnyGU","uuid":"ee548c8c-5636-452d-b0a7-57fb4b6abeef","query":{"lat_min":30,"lat_max":35,"lng_min":60,"lng_max":65,"timestamp_min":1499813608623,"timestamp_max":1499813808623}}'

query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI0MTA4MzY0ZS1iMWM4LTRmZDctOGU4Ni1mZDBlMTM4MDM5MDQifQ.N4SsfQP8thM_5DqEEPEER2AbQTYcGsPhr2HvuF4A7ho","uuid":"a397b5fe-098d-4b55-b16d-76f483cf3b26","query":{"lat_min":30,"lat_max":35,"lng_min":60,"lng_max":65,"timestamp_min":1451606400000,"timestamp_max":1452211200000}}'


r = requests.post(url = API_ENDPOINT_QUERY, data = query, verify=False)

#pastebin_url = r.text
print("Response is:%s"%r.text)
