import json
import os

from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    # YT_API_KEY скопирован из гугла и вставлен в переменные окружения
    __api_key: str = os.getenv('API_KEY')

    # создать специальный объект для работы с API
    __youtube = build('youtube', 'v3', developerKey=__api_key)

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.channel = self.__youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.channel, indent=2, ensure_ascii=False))


#vdud = Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
#vdud.print_info()
