from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage


# класс для работы со страницей создания/редактирования поста (/blog/editor/)
class PostModifyPage(BasePage):
    TITLE_FIELD = (By.ID, "title")
    TEXT_FIELD = (By.ID, "text")
    TAGS_FIELD = (By.ID, "tags")
    SUBMIT_BUTTON = (By.ID, "submit")

    def add_title(self, title):
        self.wait_until_clickable(self.TITLE_FIELD).send_keys(title)

    def change_title(self):
        self.wait_until_clickable(self.TITLE_FIELD).send_keys(Keys.BACKSPACE)

    def add_text(self, text):
        self.wait_until_clickable(self.TEXT_FIELD).send_keys(text)

    def add_tags(self, tags):
        self.wait_until_clickable(self.TAGS_FIELD).send_keys(tags)

    def click_submit_button(self):
        self.wait_until_clickable(self.SUBMIT_BUTTON).click()

        