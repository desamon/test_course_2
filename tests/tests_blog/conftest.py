import pytest

from constants import SESSION_COOKIE, Links


@pytest.fixture(autouse=True)
def login(browser):
    browser.get(Links.login)
    browser.add_cookie(SESSION_COOKIE)
    browser.refresh()
