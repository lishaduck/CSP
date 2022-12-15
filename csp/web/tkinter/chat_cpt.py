import httplib2

endpoint = input("endpoint")

http = httplib2.Http(".cache")
http.add_credentials(input("User"), input("Password"))

response, content = http.request(endpoint, "GET")

print(response.status)
print(content)
