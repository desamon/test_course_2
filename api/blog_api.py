from typing import List, Union, Dict

from api.api_client import Client


class BlogApi(Client):
    """Класс с методами для отправки api-запросов к блогу"""
    _posts = "api/posts"

    def get_user_posts(self) -> Union[Dict, None]:
        """Метод для получения всех постов пользователя"""
        return self.get(self._posts)

    def delete_post(self, post_id: int) -> Union[Dict, None]:
        """Метод для удаления поста по заданному post_id"""
        return self.delete(f"{self._posts}/{post_id}")

    def create_post(self, title: str, text: str, tags: List[str]) -> Union[Dict, None]:
        """Метод для создания поста"""
        return self.post(self._posts, body={"title": title, "text": text, "tags": tags})
