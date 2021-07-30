import requests
import json
from tqdm import tqdm


class VkClient:
    url = "https://api.vk.com/method/"

    def __init__(self, token, version):
        self.params = {
            'access_token': token,
            'v': version
        }

    def get_photo_info(self, vk_id, photo_sizes=1):
        get_list_photo_url = self.url + 'photos.get'
        get_list_photo_params = {
            'owner_id': vk_id,
            'photo_sizes': photo_sizes,
            'count': '5',
            'extended': '1',
            'album_id': 'profile'
        }
        req = requests.get(get_list_photo_url, params={**self.params, **get_list_photo_params}).json()
        return req

    def get_photo_json(self, vk_id, photo_sizes=1):
        req = self.get_photo_info(vk_id, photo_sizes)
        name_list = [str(req['response']['items'][0]['likes']['count']) + '.jpg']
        for el in tqdm(req['response']['items'][1:], desc='Формирование списка имен фото для загрузки'):
            if str(el['likes']['count']) + '.jpg' in name_list:
                name_list.append(str(el['likes']['count']) + "_" + str(el['date']) + '.jpg')
            else:
                name_list.append(str(el['likes']['count']) + '.jpg')

        link_list = []
        list_size = []
        result_json = []
        for el in tqdm(req['response']['items'], desc='Формирование списка ссылок фото для загрузки'):
            link_list.append(el['sizes'][-1]['url'])
            list_size.append(el['sizes'][-1]['type'])

        photo_dict = dict(zip(name_list, link_list))
        for filename, size in zip(name_list, list_size):
                name_dict_json = {'filename': filename,
                                  'size': size}
                result_json.append(name_dict_json)
        result_file = open('result_photo.json', 'w+', encoding='utf-8')
        json.dump(result_json, result_file, ensure_ascii=False, indent=4)
        result_file.close()

        return photo_dict
