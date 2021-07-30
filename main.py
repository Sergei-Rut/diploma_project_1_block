from vkclient import VkClient
from yandexdiskclient import YandexClient
from pprint import pprint

token_vk = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
version_vk = '5.131'

if __name__ == '__main__':
    id_vk = input('Введите id пользователя в VK:')
    token_ya = input('Введите токен для яндекс диска:')
    vk_client = VkClient(token_vk, version_vk)
    photo_data = vk_client.get_photo_json(id_vk)
    ya_client = YandexClient(token=token_ya)
    ya_client.upload(path='upload_photo_from_vk/', photo_d=photo_data)
#    photo_info = vk_client.get_photo_info(id_vk)
#    pprint(photo_data)
