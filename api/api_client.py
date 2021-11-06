from json import JSONDecodeError
from typing import Dict, Union
from http import HTTPStatus

import requests

from constants import POSITIVE_LOGIN_CREDENTIALS


def check_response(func):
   """Декоратор, который проверяет статус ответа и конвертирует ответ в json"""
   def wrapper(self, url, **kwargs):
       response = func(self, url, **kwargs)
       if response.status_code != HTTPStatus.OK:
           raise Exception("Unsuccessful response")
       try:
           return response.json()
       except JSONDecodeError:
           return None
   return wrapper


class Client:
   """Класс - апи-клиент для отправки разных типов запросов"""
   def __init__(self, url):
       self._session = None
       self._base_url = url
       self._login = self._base_url + "api/login"
       self.auth()

   def auth(self) -> Dict:
       """Метод для авторизации пользователя, создает сессию, в которой авторизуется,
       возвращает авторизационные куки"""
       self._session = requests.session()
       self._session.post(self._login, data=POSITIVE_LOGIN_CREDENTIALS)
       return self._session.cookies.get_dict()

   @check_response
   def post(self, url: str, body: Dict = None) -> Union[Dict, None]:
       """Метод для отправки POST запросов"""
       return self._session.post(self._base_url + url, data=body)

   @check_response
   def get(self, url: str) -> Union[Dict, None]:
       """Метод для отправки GET запросов"""
       return self._session.get(self._base_url + url)

   @check_response
   def delete(self, url: str, body: Dict = None) -> Union[Dict, None]:
       """Метод для отправки DELETE запросов"""
       return self._session.delete(self._base_url + url, data=body)

