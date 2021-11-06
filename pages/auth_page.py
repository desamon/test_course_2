from selenium.webdriver.common.by import By

from constants import Links
from pages.blog_pages.main_page import BasePage, MainPage


# класс для работы со страницей авторизации (/login)

class AuthPage(BasePage):
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CLASS_NAME, "button")

    def login_ui(self, email: str, password: str) -> None:
        """Функция логина на стенде через UI"""
        self.wait_until_clickable(self.EMAIL_FIELD).send_keys(email)
        self.wait_until_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_until_clickable(self.LOGIN_BUTTON).click()

    def check_profile_page_is_open(self):
        assert self.wait_for_url_to_be(self.url.replace(Links.login, Links.profile))

    def check_page_is_open(self, url):
        assert self.wait_for_url_to_be(url)

    def check_user_is_authorised(self):
        assert self.browser.get_cookie("session"), "Куки с session name отсутствует"


    def logout_auth(self, browser, url):
        self.logout_auth.logout()
        self.blog_page.open_page()
        self.blog_page.check_button_new()

