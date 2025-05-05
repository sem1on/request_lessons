import requests


response = requests.post(
    url="https://petstore.swagger.io/v2/pet",
    headers={
        "api_key": "special-key"
    },
    json={
        "id": 21,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "mimimi",
        "photoUrls": [
            "string"
        ],
        "tags": [
            {
                "id": 0,
                "name": "cat"
            }
        ],
        "status": "available"
    }
    )

get_pet_by_id = requests.get(
    url="https://petstore.swagger.io/v2/pet/21",
    headers={
        "api_key": "special-key"
    },
)

post_files = requests.post(
    url="https://petstore.swagger.io/v2/pet/21/uploadImage",
    headers={
        "api_key": "special-key"
    },
    files={
        "file": ("images.jpg", open("images.jpg", "rb"), "image/jpg")
    }
)
print(post_files.json())