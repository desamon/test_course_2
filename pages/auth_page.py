from webbrowser import Chrome
import pytest
from selenium.webdriver.common.by import By
from constants import Links
from functions import wait_until_clickable
from pages.blog_pages.main_page import BasePage, MainPage


class AuthPage(BasePage):
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.login_page = BasePage(browser, url + Links.login)
        self.blog_page = MainPage(browser, url + Links.blog)

    def login_ui(self: Chrome, email: str, password: str) -> None:
        """Функция логина на стенде через UI"""
        wait_until_clickable(self, (By.NAME, "email")).send_keys(email)
        wait_until_clickable(self, (By.NAME, "password")).send_keys(password)
        wait_until_clickable(self, (By.CLASS_NAME, "button")).click()
#выделение self пичармом - это же ошибка, а почему он выделяет?

    def logout_auth(self, browser,  url):
        logout_auth = BasePage(browser, url)
        blog_page = MainPage(browser, url)
        self.logout_auth.logout()  # нажимаем на выход
        self.blog_page.open_page() # открываем страницу блога
        self.blog_page.check_button_new()

#какие ещё методы нужно было добавить на эту страницу?