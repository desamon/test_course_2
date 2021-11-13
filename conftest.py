import pytest
import random
from constants import Links
from constants import VALID_BROWSERS, BROWSER_REMOTE_CAPABILITIES, COMMAND_EXECUTOR


@pytest.fixture()
def browser(request):
    launch = request.config.getoption("--launch")
    if launch == 'remote':
        browser = VALID_BROWSERS[launch](command_executor=COMMAND_EXECUTOR,
                                         desired_capabilities=BROWSER_REMOTE_CAPABILITIES)
    else:
        browser = VALID_BROWSERS[launch]()
    browser.maximize_window()
    yield browser
    browser.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--env", default="prod"
    )
    parser.addoption(
        "--launch", default="chrome", choices=["chrome", "opera", "remote"]
    )


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
