from hw19_2classes import PhotoApi

image_path = "photo_2025-03-21_10-51-55.jpg"

photo_api = PhotoApi()

make_post = photo_api.upload_photo_to_server(image_path)
if make_post.status_code == 201:
    print(f"Успішний POST запит {make_post.status_code}\nДодатково: {make_post._content}\n")
else:
    print(f"Запит POST неуспішний: {make_post.status_code}\nДодатково: {make_post._content}\n")


make_get = photo_api.get_photo_from_server(image_path)
if make_get.status_code == 200:
    print(f"Успішний GET запит {make_get.status_code}\nДодатково: {make_get._content}\n")
else:
    print(f"Запит GET неуспішний: {make_get.status_code}\nДодатково: {make_get._content}\n")



make_delete = photo_api.delete_photo_from_server(image_path)
if make_delete.status_code == 200:
    print(f"Успішний DELETE запит {make_delete.status_code}\nДодатково: {make_delete._content}\n")
else:
    print(f"Запит DELETE неуспішний: {make_delete.status_code}\nДодатково: {make_delete._content}\n")