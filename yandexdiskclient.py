import requests
from time import sleep
from tqdm import tqdm


class YandexClient:
    url = "https://cloud-api.yandex.net/v1/disk/resources/"

    def __init__(self, token):
        self.token = token

    def upload(self, path, photo_d):

        upload_url = self.url + 'upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        for filename, url in tqdm(photo_d.items(), desc='Закачка фото на яндекс диск'):
            sleep(.1)
            disk_file_path = path + filename
            params = {"path": disk_file_path, "url": url, "overwrite": "true"}
            response = requests.post(upload_url, headers=headers, params=params)
            response.raise_for_status()
            if response.status_code != 202:
                return print('Скачивание фото на получилось')
