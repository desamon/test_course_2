import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from constants import POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS, Links
from functions import wait_until_clickable, wait_for_url_to_be, login_ui, wait_until_visible


@pytest.mark.auth
class TestAuthorizationClass:
    @pytest.mark.smoke
    def test_login_positive(self, browser, email, password):
        browser.get(Links.login)
        browser.maximize_window()
        remember_me_checkbox = wait_until_visible(browser, (
        By.CSS_SELECTOR, ".checkbox input"))  # проверяем, не включен ли он по умолчанию

        assert not remember_me_checkbox.get_attribute("checked"), "Чекбокс включен по умолчанию"

        remember_me_checkbox.click()
        login_ui(browser, email, password)
        wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/profile')

        assert browser.get_cookie("session"), "Куки с session name отсутствует"

    @pytest.mark.smoke
    @pytest.mark.parametrize("email, password", NEGATIVE_LOGIN_CREDENTIALS,
                             ids=["negative email, positive password", "positive email, negative password",
                                  "not valid email, positive password", "not valid data"])
    def test_login_negative(self, browser, email, password):
        browser.get(Links.login)
        browser.maximize_window()
        login_ui(browser, email, password)
        wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()
        WebDriverWait(browser, 5)

        assert wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/login'), "Отображается не страница входа"

