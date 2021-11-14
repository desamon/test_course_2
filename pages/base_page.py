from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


# класс с общими хэлперами и методами для работы с элементами, которые расположены на каждой странице
class BasePage:
    LOGOUT = (By.CSS_SELECTOR, "a[href*='/logout']")

    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def logout(self):
        self.wait_until_clickable(self.LOGOUT).click()

    def wait_for_url_to_be(self, url: str, timeout: int = 5) -> bool:
        """Ждём, пока URL страницы не начнёт соответствовать ожидаемому"""
        return WebDriverWait(self.browser, timeout).until(ec.url_to_be(url))

    def page_title_is(self, title: str, timeout: int = 5) -> bool:
        """Ждём, пока заголовок веб-страницы (title) не начнёт соответствовать ожидаемому"""
        return WebDriverWait(self.browser, timeout).until(ec.title_is(title))

    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        """Ждём, пока элемент не станет видимым и кликабельным"""
        return WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable(locator))

    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        """Ждём, пока элемент не появится в DOM"""
        return WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))

    def wait_until_not_present(self, locator: Tuple, timeout=5) -> WebElement:
        """Ждём, когда элемента не будет на странице"""
        return WebDriverWait(self.browser, timeout).until_not(ec.presence_of_element_located(locator))

    def wait_until_visible(self, locator: Tuple, timeout: int = 5):
        """Ждём, пока элемент не станет видимым"""
        return WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located(locator))

    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        """Убеждаемся, что элемент присутствует на странице"""
        try:
            self.wait_until_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    def check_user_is_authorised(self):
        assert self.browser.get_cookie("session"), "Куки с session name отсутствует"
