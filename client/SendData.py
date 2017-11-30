#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "https://localhost:8080/api/data"

# data to be sent to api
data = "{\"data\":[{\"uuid\":\"0fd115a6-8228-4c35-9f4f-7144519d0a76\",\"timestamp\":1499813708623,\"value\":15,\"geometryType\":\"point\",\"coordinates\":[[30,60]]}]}"

# Sending Data
r = requests.post(url = API_ENDPOINT, data = data, verify=False)

# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)


#query the data from the API
API_ENDPOINT_QUERY = "https://localhost:8080/api/querydata"


#query to be send to api
query="{\"query\":{\"lat_min\":29,\"lat_max\":31,\"lng_min\":59,\"lng_max\":61,\"timestamp_min\":1499813608623,\"timestamp_max\":1499813808623}}"

r = requests.post(url = API_ENDPOINT_QUERY, data = query, verify=False)

pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
