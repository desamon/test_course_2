from typing import Tuple

from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


def wait_for_url_to_be(driver: Chrome, url: str, timeout: int = 5) -> bool:
   """Ждём, пока URL страницы не начнёт соответствовать ожидаемому"""
   return WebDriverWait(driver, timeout).until(ec.url_to_be(url))


def page_title_is(driver: Chrome, title: str, timeout: int = 5) -> bool:
   """Ждём, пока заголовок веб-страницы (title) не начнёт соответствовать ожидаемому"""
   return WebDriverWait(driver, timeout).until(ec.title_is(title))


def wait_until_clickable(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
   """Ждём, пока элемент не станет видимым и кликабельным"""
   return WebDriverWait(driver, timeout).until(ec.element_to_be_clickable(locator))


def wait_until_present(driver: Chrome, locator: Tuple, timeout: int = 5) -> WebElement:
   """Ждём, пока элемент не появится в DOM"""
   return WebDriverWait(driver, timeout).until(ec.presence_of_element_located(locator))


def wait_until_not_present(driver: Chrome, locator: Tuple, timeout=5) -> WebElement:
   """Ждём, когда элемента не будет на странице"""
   return WebDriverWait(driver, timeout).until_not(ec.presence_of_element_located(locator))


def wait_until_visible(driver: Chrome, locator: Tuple, timeout: int = 5):
   """Ждём, пока элемент не станет видимым"""
   return WebDriverWait(driver, timeout).until(ec.visibility_of_element_located(locator))


def element_is_present(browser: Chrome, locator: Tuple, timeout: int = 5) -> bool:
   """Убеждаемся, что элемент присутствует на странице"""
   try:
       wait_until_visible(browser, locator, timeout)
       return True
   except TimeoutException:
       return False

def login(browser: Chrome, email: str, password: str) -> None:
   """Функция логина на стенде без использования ожиданий"""
   email = browser.find_element(By.NAME, "email")
   email.send_keys("qa_test@test.ru")
   password = browser.find_element(By.NAME, "password")
   password.send_keys("!QAZ2wsx")
   browser.find_element(By.CLASS_NAME, "button").click()

   