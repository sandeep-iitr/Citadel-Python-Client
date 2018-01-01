#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/point"

sensor = '{"query":{"pointType":"temp","unit":"F"}}'

# Sending Data
r = requests.post(url = API_ENDPOINT, data = sensor,verify=False)

print("The Response is:%s"%r.text)


#querying the Sensor just inserted.

#API_ENDPOINT_QUERY = "https://localhost:8080/api/query"


#query = "{\"query\":{\"userToken\":\"e17e176a-8830-4075-ad0a-7e74963ac7e5\",\"uuid\":\"e617d1a1-6323-4d5d-b66a-a63ab70ca349\"}}";

# Sending query
#r = requests.post(url = API_ENDPOINT_QUERY, data = query,verify=False)

#pastebin_url = r.text
#print("The pastebin URL is:%s"%pastebin_url)

