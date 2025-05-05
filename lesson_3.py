import requests


response = requests.patch(
    url="https://jsonplaceholder.typicode.com/posts/1",
    json={
        "title": "QWE"
    }
)

print(response.json())