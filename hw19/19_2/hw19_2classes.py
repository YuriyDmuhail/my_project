import os
from dotenv import load_dotenv
import requests
from requests import Response
from pathlib import Path
from urllib.parse import quote

env_path = Path("new.env")
load_dotenv(dotenv_path=env_path)
base_url = os.getenv("bs_url")



class BaseApi:
    base_url = os.getenv("bs_url")

    def _get(self, endpoint: str, headers):
        return requests.get(url=endpoint, headers=headers)

    def _post(self, endpoint: str, files: dict):
        return requests.post(url=endpoint, files=files)

    def _delete(self, endpoint: str):
        return requests.delete(url=endpoint)


class PhotoApi(BaseApi):
    EDPOINT: str = f"{BaseApi.base_url}"

    def upload_photo_to_server(self, image_file): # /upload
        with open(image_file, "rb") as image_file:
            files = {
                "image": image_file
            }
            return self._post(endpoint=f"{self.EDPOINT}/upload", files= files)

    def get_photo_from_server(self, file_name):  #/image/<filename>
        head = {'Content-Type': 'text'}
        return self._get(endpoint=f"{self.EDPOINT}/image/{file_name}", headers=head)

    def delete_photo_from_server(self, filename):  #/delete/<filename>
        return self._delete(endpoint=f"{self.EDPOINT}/delete/{filename}")



