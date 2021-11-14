import pytest
from api.api_client import Client


@pytest.fixture(autouse=True)
def login(browser, url):
    cookie = Client(url).auth()
    browser.get(url)
    browser.add_cookie({"name": "session", "value": cookie["session"]})
    browser.refresh()

