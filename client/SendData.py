# importing the requests library
import requests
 
# defining the api-endpoint 
API_ENDPOINT = "http://localhost:8080/api/data"

# data to be sent to api
data = "{\"data\":[{\"uuid\":\"xxxx\",\"timestamp\":1499813708623,\"value\":15,\"geometryType\":\"point\",\"coordinates\":[[30,60]]}]}"
#length = len(data)
#print(length)
#headers = {'content-type': 'application/json','Content-Lenght':'110'}
# sending post request and saving response as response object
#r = requests.post(url = API_ENDPOINT, data = data,headers=headers)

r = requests.post(url = API_ENDPOINT, data = data)

# extracting response text 
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)


#query the data from the API
API_ENDPOINT_QUERY = "http://localhost:8080/api/querydata"


#query to be send to api
query="{\"query\":{\"lat_min\":10,\"lat_max\":90,\"lng_min\":10,\"lng_max\":90,\"timestamp_min\":1499813608623,\"timestamp_max\":1499813808623}}"

r = requests.post(url = API_ENDPOINT_QUERY, data = query)

pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)
