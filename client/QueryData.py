#cleaning up the Hbase Database: note it will delete all the tables
#echo 'list.each {|t| disable t; drop t}; quit;' | ./bin/hbase shell

# importing the requests library
import requests
import json

#query the data from the API
#API_ENDPOINT_QUERY = "https://citadel.westus.cloudapp.azure.com:8080/api/querydata"
API_ENDPOINT_QUERY = "https://localhost:8080/api/querydata"


#Query by citadel.ucla@gmail.com
#query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI2OGUyZDk3Yy0yYjBlLTRjZmUtYTIzOC1jMzEyMjFmZTIwYWMifQ.IR2yHOcOXkiMaCWFduOLjKxGLRkHhRJj_hsiand1CgQ","uuid":"67913068-4557-45cd-bed2-4d50d714d7aa","query":{"lat_min":30,"lat_max":30.1,"lng_min":60,"lng_max":60.1,"timestamp_min":1451606400000,"timestamp_max":1463142400000}}'

#Query by: testcitadel1
query='{"userToken":"eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3YzgxYjlhZS1kYmJjLTRjZTYtYjE0ZC1kNjBjZWY5Mzc1MDcifQ.lePmyCrFhYA7MG2DkhtsC97Gbk784puPW4ghQit_QZY","uuid":"67913068-4557-45cd-bed2-4d50d714d7aa","query":{"lat_min":30,"lat_max":30.1,"lng_min":60,"lng_max":60.1,"timestamp_min":1451606400000,"timestamp_max":1463142400000}}'


r = requests.post(url = API_ENDPOINT_QUERY, data = query, verify=False)

pastebin_url = r.text
print("Response is:%s"%r.text)
