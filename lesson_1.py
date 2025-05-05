import requests


response = requests.get(
    url="https://petstore.swagger.io/v2/pet/findByStatus",
    headers={
        "api_key": "special-key"
    },
    params={
        "status": "sold"
    }
    )
print(response.json())
print(response.status_code)
