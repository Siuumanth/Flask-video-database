import requests
import json

BASE = "http://127.0.0.1:5000/"

headers={'Content-Type': 'application/json'}
data=[{"name":"umm1","views":123,"likes":76},
      {"name":"umm2","views":155,"likes":756},
      {"name":"umm3","views":122,"likes":330}]


for i in range(len(data)):
    json_data=json.dumps(data[i])

    response=requests.put(BASE + "video/" + str(i) , data=json_data , headers=headers)    #its a form
    try:
        umm = response.json()
        print(umm)
    except json.decoder.JSONDecodeError as e:
        print("Error decoding JSON:", e)
#now,data is created using put request and stored in dictionary
a=input()

response=requests.get(BASE + "video/" + a )    #its a form
print(response.json())
#now we call those values back from the dictionary get method




