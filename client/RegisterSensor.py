#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/point"

sensor = '{"name":"temp","unit":"F"}'

# Sending Data
r = requests.post(url = API_ENDPOINT, data = sensor,verify=False)

print("The Response is:%s"%r.text)


#querying the Sensor just inserted.

API_ENDPOINT_QUERY = "https://localhost:8080/api/query"


query = '{"query":{"uuid":"46d5f807-bfde-48d9-af59-fa4c9ae88051"}}';

# Sending query
r = requests.post(url = API_ENDPOINT_QUERY, data = query,verify=False)

print("The Response is:%s"%r.text)

