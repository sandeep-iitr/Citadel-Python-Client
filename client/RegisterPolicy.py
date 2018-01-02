#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

#start mongodb: sudo mongod --dbpath=/home/sandeep/MetroInsight/installation/mongo-data
#May need to kill previous instances
#sudo killall -15 mongod


# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8089/api/registerPolicy"

#API_ENDPOINT = "https://citadel.westus.cloudapp.azure.com:8089/api/registerPolicy"

Policy = '{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI5ZjBmZGNjNC1mY2VmLTRhY2QtYjQ4ZC03MTEwYjgzMzFjZGIifQ.B83WC1EJpPmmZ9rS6S8u9vJHEOiS61wwMmTWLuidnCE","policy":{"sensors":["d259fe92-c3d8-4ff3-a00e-915f178aafa0"], "users":["testcitadel1@gmail.com"]}}'

r = requests.post(url = API_ENDPOINT, data = Policy,verify=False)
print("Response is:%s"%r.text)
