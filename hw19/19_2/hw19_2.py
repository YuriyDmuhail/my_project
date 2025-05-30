import os
from dotenv import load_dotenv
import requests
from requests import Response
from pathlib import Path
from urllib.parse import quote

env_path = Path("new.env")
load_dotenv(dotenv_path=env_path)
base_url = os.getenv("bs_url")

image_path = "photo_2025-03-21_10-51-55.jpg"

class BaseApi:
    base_url = os.getenv("bs_url")

    def _get(self, endpoint: str,**kwargs):
        return requests.get(url=endpoint)

    def _post(self, endpoint: str, files: dict):
        return requests.post(url=endpoint, files=files)

    def _delete(self, endpoint: str):
        return requests.delete(url=endpoint)


class PhotoApi(BaseApi):
    EDPOINT: str = f"{BaseApi.base_url}"

    def upload_photo(self, image_file): # /upload
        with open(image_file, "rb") as image_file:
            files = {
                "image": image_file
            }
            return self._post(endpoint=f"{self.EDPOINT}/upload", files= files)

    def get_photo(self, file_name):  #/image/<filename>
        head = {'Content-Type': 'text'}
        return self._get(endpoint=f"{self.EDPOINT}/image/{file_name}", headers=head)

    def delete_photo(self, filename):  #/delete/<filename>
        return self._delete(endpoint=f"{self.EDPOINT}/delete/{filename}")





def do_post_req(data):
    """
    Post запит
    """
    make_post = PhotoApi().upload_photo(data)
    if make_post.status_code == 201:
        return print(f"Успішний POST запит {make_post.status_code}\nДодатково: {make_post._content}\n")
    else:
        return print(f"Запит POST неуспішний: {make_post.status_code}\nДодатково: {make_post._content}\n")

def do_get_req(data):
    """
    Get запит
    """
    make_get = PhotoApi().get_photo(data)
    if make_get.status_code == 200:
        return print(f"Успішний GET запит {make_get.status_code}\nДодатково: {make_get._content}\n")
    else:
        return print(f"Запит GET неуспішний: {make_get.status_code}\nДодатково: {make_get._content}\n")


def do_delete_req(data):
    """
    Delete запит
    """
    make_delete = PhotoApi().delete_photo(data)
    if make_delete.status_code == 200:
        return print(f"Успішний DELETE запит {make_delete.status_code}\nДодатково: {make_delete._content}\n")
    else:
        return print(f"Запит DELETE неуспішний: {make_delete.status_code}\nДодатково: {make_delete._content}\n")


do_post_req(image_path)
do_get_req(image_path)
do_delete_req(image_path)