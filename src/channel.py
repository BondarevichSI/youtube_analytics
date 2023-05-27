import os
import json
from googleapiclient.discovery import build


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self.channel_id = channel_id

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        # API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('API_KEY')
        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        # получить данные о канале по его id
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        # Выводит словарь в json-подобном удобном формате с отступами
        print(json.dumps(channel, indent=2, ensure_ascii=False))
