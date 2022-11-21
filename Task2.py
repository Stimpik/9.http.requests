import requests


class YaUploader:
    base_host = 'https://cloud-api.yandex.net:443/'

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        uri = 'v1/disk/resources/upload'
        request_url = self.base_host + uri
        headers = {'Authorization': f'OAuth {token}'}
        for file in file_path:
            params = {'path': f'/homework/{file.split("/")[-1]}', 'overwrite': True}
            response = requests.get(request_url, headers=headers, params=params)
            requests.put(response.json()['href'], data=open(file, 'rb'), headers=headers)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ['C:/Users/stimp/Desktop/Моя халтура/СЗГЭ.txt', 'C:/Users/stimp/Desktop/2.txt']
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
