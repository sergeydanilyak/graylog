# api_key = "your_token"
# params = {"selected_grantee_capabilities":{"grn::::user:613875f68e4b480eeea31e6b":"view"}}
    #    {"selected_grantee_capabilities":{"grn::::user:61bc3ae01d634d4909edbd03":"view"}}
# url_api = 'https://log.dispatchland.com/api/authz/shares/entities/grn::::stream:618a5772c3c915212e63edcb'
# head = {
#     'X-Requested-By':'*',
#     'Content-type':'application/json',
#     # 'Accept':'text/plain'
#       }
# response = requests.post(url_api, auth=(api_key, 'token'), data=json.dumps(params), headers=head)
# print(response.status_code)


# curl -u your_token:token -X GET 'https://log.dispatchland.com/api/users'

# curl -u your_token:token -X POST 'https://log.dispatchland.com/api/authz/shares/entities/grn::::stream:618a5772c3c915212e63edcb' -H 'X-Requested-By:*' -H 'Content-Type: application/json' --data-raw '{"selected_grantee_capabilities":{"grn::::user:613875f68e4b480eeea31e6b":"view"}}'

# import pprint
import requests
import json
from requests.auth import HTTPBasicAuth
from getpass import getpass

# # # ...
url = "https://log.dispatchland.com/api"
api_key = "your_token"
head = {
    'X-Requested-By':'*',
    'Content-type':'application/json',
    # 'Accept':'text/plain'
      }

# # # ...

url_api = "/users"
user_id = []
# grn_users = []
params = []
user_grn = []
users = requests.get(url+url_api, auth=(api_key, 'token'), headers=head)
# print(users.status_code)
users = users.json()["users"]
for i in users:
    user_id.append(i["id"])
user_id.remove('615576d8814e3229cf542b80')
# print (user_id)
# test = "test"
# user_id.remove('"grn::::user:local:admin":"view"')
user_id.pop(0)
user_grn = list(map(lambda x: '"grn::::user:'+x+'":"view"', user_id))
# print(user_grn)
user_grn = ",".join(user_grn)
params = '{"selected_grantee_capabilities":{'+user_grn+'}}'
# params = ",".join(params)
print(params)
# params = list(map(lambda x: '{"selected_grantee_capabilities":{"grn::::user:'+x+'":"view"}}', user_id))

# # # .....

url_api = "/streams"
stream = requests.get(url+url_api, auth=(api_key, 'token'), headers=head)
# print(stream.status_code)
stream_id = []
url_stream = []
stream = stream.json()["streams"]
for j in stream:
       stream_id.append(j['id'])
# print (stream_id)
# url_stream = list(map(lambda x: 'grn::::stream::' + x, stream_id))
url_stream = list(map(lambda x: 'https://log.dispatchland.com/api/authz/shares/entities/grn::::stream:'+x, stream_id))
    # print (url_stream)
for url in url_stream:
    # for param in params:
      response = requests.post(url, auth=(api_key, 'token'), data=params, headers=head)  
    #   print(response.status_code)
      print(response.content)
# # # ...