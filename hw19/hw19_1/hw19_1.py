import requests
import json

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

response = requests.get(url, params = params)

if response.status_code == 200:
    data = response.json()

    for item in data.get("photos", []):
        photo_url = item.get("img_src")
        request_photo = requests.get(photo_url)

        if request_photo.status_code == 200:
            with open("photo_url", "wb") as file:
                file.write(response.content)
        else:
            print('Не вдалося зробити запит. Код помилки:', request_photo.status_code)
else:
    print('Не вдалося зробити запит. Код помилки:', response.status_code)

