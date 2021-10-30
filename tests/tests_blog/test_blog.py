from selenium.webdriver.common.by import By

from constants import Links
from functions import wait_until_clickable, wait_until_visible


class TestBlog:
    def test_post_blog(self, browser, login):
        browser.get(Links.blog)
        wait_until_clickable(browser, (By.CSS_SELECTOR, '[href="/blog/page/1/test-post/"]')).click()
        post_text = wait_until_visible(browser,(By.CSS_SELECTOR, ".container p+p"))
        assert post_text.text == "Hello world!", "Неверный текст!"
