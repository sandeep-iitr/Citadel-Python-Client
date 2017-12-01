#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/point"

sensor = "{\"query\":{\"userToken\":\"e1e7013a-fb31-4087-8019-8d210396867a\",\"pointType\":\"temp\",\"unit\":\"F\"}}"

# Sending Data
#r = requests.post(url = API_ENDPOINT, data = sensor,verify=False)

# extracting response text 
#pastebin_url = r.text
#print("The pastebin URL is:%s"%pastebin_url)
#a318e0a7-4c79-417c-ad8b-b1c96c55c453

#The pastebin URL is:{"result":"SUCCESS","uuid":"0fd115a6-8228-4c35-9f4f-7144519d0a76"}

#querying the Sensor just inserted.

API_ENDPOINT_QUERY = "https://localhost:8080/api/query"

query = "{\"query\":{\"uuid\":\"a318e0a7-4c79-417c-ad8b-b1c96c55c453\"}}";

# Sending query
r = requests.post(url = API_ENDPOINT_QUERY, data = query,verify=False)

pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

