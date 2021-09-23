import requests

#listing json user data
query={'page':1}
response_get = requests.get("https://reqres.in/api/users",params=query)
print(response_get.json())
print("\n")

for id in response_get.json()['data']:
    print(f"{id['first_name']} {id['last_name']}")
print('\n\n')

#getting a single user
query={'id':'2'}
response_get = requests.get("https://reqres.in/api/users",params=query)
print(response_get.json())
print("\n")

#create data at api site
response_post = requests.post("https://reqres.in/api/users",data={'name':'Harshal','job':'Intern'})
print(response_post.json())
print("\n")

#update data -put
response_put = requests.put("https://reqres.in/api/users/2",data={'name':'Harshal','job':'Intern'})
print(response_put.json())
print("\n")

#update data -patch
response_patch = requests.patch("https://reqres.in/api/users/2",data={'name':'Harshal','job':'Intern'})
print(response_patch.json())
print("\n")

#register
response_reg = requests.post("https://reqres.in/api/register",{"email": "eve.holt@reqres.in","password": "pistol"})
print(response_reg.json())
print("\n")

#login
response_login = requests.post("https://reqres.in/api/login",{"email": "eve.holt@reqres.in","password": "pistol"})
print(response_login.json())
print("\n")

#delete
response_delete = requests.delete("https://reqres.in/api/users/2")
print(response_delete)
print("\n")
