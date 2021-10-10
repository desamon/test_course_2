import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from functions import wait_until_clickable
from selenium.webdriver.support import expected_conditions as ec
from data import data_for_test

@pytest.mark.auth
class TestAuthorizationClass:

   @pytest.mark.smoke
   def test_login_positive(self):
       with Chrome() as browser:
           browser.get('https://qastand.valhalla.pw/login')
           browser.maximize_window()
           wait_until_clickable(browser, (By.NAME, "email")).send_keys("qa_test@test.ru")
           wait_until_clickable(browser, (By.NAME, "password")).send_keys("!QAZ2wsx")
           remember_me_checkbox = browser.find_element(By.CSS_SELECTOR, ".checkbox input")
           #проверяем, не включен ли он по умолчанию
           assert not remember_me_checkbox.get_attribute("checked"), "Чекбокс включен по умолчанию"

           remember_me_checkbox.click()
           wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()
           wait = WebDriverWait(browser, 5)
           wait.until(ec.url_to_be('https://qastand.valhalla.pw/profile'))

           assert browser.get_cookie("session"), "Куки с session name отсутствует"


   @pytest.mark.smoke
   @pytest.mark.parametrize("email, password", data_for_test,
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
           assert wait.until(ec.url_to_be('https://qastand.valhalla.pw/login')), "Отображается не страница входа"

