import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functions import wait_until_clickable, wait_for_url_to_be, login, wait_until_visible
from selenium.webdriver.support import expected_conditions as ec
from data import negative_login, positive_login


@pytest.mark.auth
class TestAuthorizationClass:
   @pytest.mark.smoke
   def test_login_positive(self):
       with Chrome() as browser:
           browser.get('https://qastand.valhalla.pw/login')
           browser.maximize_window()
           remember_me_checkbox = wait_until_visible(browser, (By.CSS_SELECTOR, ".checkbox input"))
           # проверяем, не включен ли он по умолчанию

           assert not remember_me_checkbox.get_attribute("checked"), "Чекбокс включен по умолчанию"

           remember_me_checkbox.click()
           login(browser, positive_login ["email"], positive_login["password"])

           wait = WebDriverWait(browser, 5)
           wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/profile')

           assert browser.get_cookie("session"), "Куки с session name отсутствует"


   @pytest.mark.smoke
   @pytest.mark.parametrize("email, password", negative_login,
                                   ids=["negative email, positive password", "positive email, negative password",
                                        "not valid email, positive password", "not valid data"])
   def test_login_negative(self, email, password):
       with Chrome() as browser:
           browser.get('https://qastand.valhalla.pw/login')
           browser.maximize_window()
           email = wait_until_clickable(browser, (By.NAME, "email"))
           password = wait_until_clickable(browser, (By.NAME, "password"))
           wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()
           wait = WebDriverWait(browser, 5)
           assert wait_for_url_to_be(browser,'https://qastand.valhalla.pw/login'), "Отображается не страница входа"

