import pytest
from selenium.webdriver import Chrome

@pytest.fixture()
def browser():
   browser = Chrome()
   yield browser
   browser.quit()

