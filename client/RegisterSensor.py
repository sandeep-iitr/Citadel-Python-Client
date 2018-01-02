#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod

#start Virtuoso
#/media/sandeep/2Tb/sandeep/MetroInsight/installation/virtuoso/virtuoso-installed/bin/virtuoso-t -f &


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/point"

#sensor = '{"name":"temp","unit":"F"}'
Sensor = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5ZjBmZGNjNC1mY2VmLTRhY2QtYjQ4ZC03MTEwYjgzMzFjZGIifQ.B83WC1EJpPmmZ9rS6S8u9vJHEOiS61wwMmTWLuidnCE","sensor":{"name":"temperature1","unit":"F"}}'

# Sending Data
r = requests.post(url = API_ENDPOINT, data = Sensor,verify=False)

print("The Response is:%s"%r.text)


#querying the Sensor just inserted.

API_ENDPOINT_QUERY = "https://localhost:8080/api/query"


query = '{"query":{"name":"temperature1"}}';

# Sending query
r = requests.post(url = API_ENDPOINT_QUERY, data = query,verify=False)

print("The Response is:%s"%r.text)

