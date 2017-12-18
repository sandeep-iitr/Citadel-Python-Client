#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
#API_ENDPOINT = "https://localhost:8089/api/registerPolicy"

API_ENDPOINT = "https://citadel.westus.cloudapp.azure.com:8089/api/registerPolicy"

Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkYmI2YWQ0My0yZDA2LTQ3OWEtOGE1Yy05NDJkZjM3YThjODgifQ.x-9hwjTm8JQ7tsqRTSb0G_qn1CWA9xZKhCYefdMvBHc","policy":{"sensors":["302ce0e0-80d4-4b0e-8c3e-c76fb756d4be"], "users":["testcitadel1@gmail.com"]}}'

r = requests.post(url = API_ENDPOINT, data = Policy,verify=False)
print("Response is:%s"%r.text)
