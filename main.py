import requests, json, yadisk # импорт библиотек
from config import token_ya, VK_USER_ID, VK_TOKEN # импорт token_ya, VK_USER_ID, VK_TOKEN из файла config.py


def get_foto_data(count=5):  # получить информацию по первым 5 фотографиям
    api = requests.get("https://api.vk.com/method/photos.getAll", params={
        'owner_id': VK_USER_ID,
        'access_token': VK_TOKEN,
        'count': count,
        'photo_sizes': 0,
        'v': 5.131
    })
    return json.loads(api.text) # загрузка словаря с полученными данными


def get_foto():
    data = get_foto_data() # вызов функции get_foto_data, результат ее работы (это словарь) записан в переменную data
    count_foto = data["response"]["count"] # подсчет количества загруженных фотографий
    i = 0
    for files in data["response"]["items"]: # Цикл for. Перебор элементов словаря
        file_url = files["url"]   # полученная в цикле ссылка на фотографию записывается в переменную file_url
        upload = requests.get(f'{file_url}/upload?path={"https://cloud-api.yandex.net/v1/disk/resources/upload?path=%2Fimages&url=https%3A%2F%2Fsun9-31.userapi.com%2Fimpg%2FCB4PPFMMjUZOq2uTnCYXV5Yu0nASMbJNiqEtDQ%2FZKMMicTOdW0.jpg%3Fsize%3D75x34%26quality%3D95%26sign%3De434eb50665f13b4a755d01c2f735fc6%26c_uniq_tag%3DCjt2pEeu1d23MqCLGNfEwiwW2FMH7JurKpdcXqrHFs8%26type%3Dalbum"}&overwrite={False}').json()
        """Загрузка файла.
           1. savefile: ссылка на загружаемый фвйл
           2. path: Путь к загружаемому файлу (протестировала ссылку на Полигоне https://yandex.ru/dev/disk/poligon)
           3. overwrite: true or false Замена файла на Диске"""


def main(): # вызов функции main
    print(get_foto_data()) # вызов и print в консоль функции get_foto_data
    get_foto() # вызов функции get_foto


if __name__ == "__main__": # точка входа
    main()
















