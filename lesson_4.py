import requests


session = requests.Session()


response = session.get("https://httpbin.org/cookies/set?freeform=123")
print(response.json())

response = session.get("https://httpbin.org/cookies")
print(response.json())
