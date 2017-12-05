#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8089/api/registerPolicy"

sensor = "{\"userToken\":\"bd694827-8665-45c6-ad2e-720e15385934\",\"what\":[\"bacfa2ba-df15-4d1c-9575-d32c47ed24a1\"], \"whom\":[\"testcitadel1@gmail.com\",\"testcitadel3@gmail.com\"]}"


#37db5441-19cb-47b2-87a9-3f9b0232ca78

# Sending Data
r = requests.post(url = API_ENDPOINT, data = sensor,verify=False)

# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
#The pastebin URL is:{"result":"SUCCESS","uuid":"e617d1a1-6323-4d5d-b66a-a63ab70ca349"}
