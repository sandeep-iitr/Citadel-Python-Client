#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "http://localhost:8080/api/point"

sensor = "{\"query\":{\"pointType\":\"temp\",\"unit\":\"F\"}}"

# Sending Data
r = requests.post(url = API_ENDPOINT, data = sensor)

# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)

#The pastebin URL is:{"result":"SUCCESS","uuid":"0fd115a6-8228-4c35-9f4f-7144519d0a76"}
