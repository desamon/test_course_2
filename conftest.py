from selenium.webdriver import Chrome
from constants import Links
from api.api_client import Client
import random
import pytest


@pytest.fixture()
def browser():
   browser = Chrome()
   browser.maximize_window()
   yield browser
   browser.quit()


@pytest.fixture(scope="session")
def url(request):
   """Фикстура для получения заданного из командной строки окружения"""
   env = request.config.getoption("--env")
   url = Links.base_url.get(env)
   if not url:
       raise Exception("Передано неверное окружение")
   return url


def pytest_configure(config):
   config.addinivalue_line(
       "markers", "auth: tests for auth testing"
   )
   config.addinivalue_line(
       "markers", "smoke: tests for smoke testing"
   )


def pytest_addoption(parser):
   parser.addoption(
       "--env", default="prod"
   )


@pytest.fixture(scope='session', autouse=True)
def faker_seed():
   return random.randint(0, 9999)


@pytest.fixture()
def login(browser, url):
    cookie = Client(url).auth()
    browser.get(url)
    browser.add_cookie({"name": "session", "value": cookie["session"]})
    browser.refresh()

