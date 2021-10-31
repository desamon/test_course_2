import pytest
from selenium.webdriver.common.by import By
from constants import NEGATIVE_LOGIN_CREDENTIALS, Links, POSITIVE_LOGIN_CREDENTIALS
from functions import wait_until_clickable, wait_for_url_to_be, login_ui


@pytest.mark.auth
class TestAuthorizationClass:
    @pytest.mark.smoke
    def test_login_positive(self, browser, url):
        browser.get(url + Links.login)
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS["email"], POSITIVE_LOGIN_CREDENTIALS["password"])
        wait_for_url_to_be(browser, url + Links.profile)
        assert browser.get_cookie("session"), "Куки с session name отсутствует"

    @pytest.mark.smoke
    @pytest.mark.parametrize("email, password", NEGATIVE_LOGIN_CREDENTIALS,
                             ids=["negative email, positive password", "positive email, negative password",
                                  "not valid email, positive password", "not valid data"])
    def test_login_negative(self, browser, email, password):
        browser.get(Links.login)
        login_ui(browser, email, password)
        wait_until_clickable(browser, (By.CLASS_NAME, "button"))

