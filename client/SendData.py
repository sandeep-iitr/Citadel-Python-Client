#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/data"

# data to be sent to api
data = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5ZjBmZGNjNC1mY2VmLTRhY2QtYjQ4ZC03MTEwYjgzMzFjZGIifQ.B83WC1EJpPmmZ9rS6S8u9vJHEOiS61wwMmTWLuidnCE","data":[{"uuid":"d259fe92-c3d8-4ff3-a00e-915f178aafa0","timestamp":1499813708623,"value":15,"geometryType":"point","coordinates":[[60,30]]},{"uuid":"d259fe92-c3d8-4ff3-a00e-915f178aafa0","timestamp":1499813708623,"value":15,"geometryType":"point","coordinates":[[60,30]]}]}'

# Sending Data
#r = requests.post(url = API_ENDPOINT, data = data, verify=False)

#print("Response is:%s"%r.text)


#query the data from the API
API_ENDPOINT_QUERY = "https://localhost:8080/api/querydata"

#"uuids":["d259fe92-c3d8-4ff3-a00e-915f178aafa0"]

#query to be send to api
query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3NTExZGFhMC1hNzdkLTQ4MTYtOGU0OC1lYjU3ODYyY2U4YTAifQ.MKrj4ZcH4iYTU8r18urJw1H67EraZY0KEvB8b0RDVSE","query":{"lat_min":29,"lat_max":31,"lng_min":59,"lng_max":61,"timestamp_min":1499813608623,"timestamp_max":1499813808623}}'

r = requests.post(url = API_ENDPOINT_QUERY, data = query, verify=False)
print("Response is:%s"%r.text)
