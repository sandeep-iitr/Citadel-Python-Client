# importing the requests library
import requests
import json

#query the data from the API
API_ENDPOINT_QUERY = "https://citadel.westus.cloudapp.azure.com:8080/api/querydata"


#Query by citadel.ucla@gmail.com
query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJkYmI2YWQ0My0yZDA2LTQ3OWEtOGE1Yy05NDJkZjM3YThjODgifQ.x-9hwjTm8JQ7tsqRTSb0G_qn1CWA9xZKhCYefdMvBHc","uuid":"302ce0e0-80d4-4b0e-8c3e-c76fb756d4be","query":{"lat_min":30,"lat_max":30.1,"lng_min":60,"lng_max":60.1,"timestamp_min":1451606400000,"timestamp_max":1463142400000}}'

#Query by: testcitadel1
#query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzgxYjlhZS1kYmJjLTRjZTYtYjE0ZC1kNjBjZWY5Mzc1MDcifQ.lePmyCrFhYA7MG2DkhtsC97Gbk784puPW4ghQit_QZY","uuid":"302ce0e0-80d4-4b0e-8c3e-c76fb756d4be","query":{"lat_min":30,"lat_max":30.1,"lng_min":60,"lng_max":60.1,"timestamp_min":1451606400000,"timestamp_max":1463142400000}}'


r = requests.post(url = API_ENDPOINT_QUERY, data = query, verify=False)

pastebin_url = r.text
print("Response is:%s"%r.text)
