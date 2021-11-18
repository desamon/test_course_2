from selenium.webdriver import Opera, Chrome, Remote

VALID_BROWSERS = {
   "chrome": Chrome,
   "opera": Opera,
   "remote": Remote
}

BROWSER_REMOTE_CAPABILITIES = {
      "browserName": "chrome",
      "version": "95.0",
      "enableVNC": True,
  }

COMMAND_EXECUTOR = 'http://localhost:4444/wd/hub'

NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

POSITIVE_LOGIN_CREDENTIALS = {"email": "api_user_7@test.ru",
                              "password": "q7w7e7"}


class Links:
    base_url = {"prod": "https://qastand.valhalla.pw/",
                "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"


SESSION_COOKIE = {'name': 'session',
                  'value': '.eJwlzjsOwjAMANC7ZGawHX-SXqaKY0ewtnRC3J1KTG99n7KvI89n2d7HlY-yv6JsBaMOY1RaQNzqSp05QsSpazaXI'                  'FATqiOH1qnCbI3SQRHSAmG26k1o9NWhMknrWN37jU0IU45wme5GiyWBHLkj8mzc09y03JHrzOO_ofL9AVk6Le8.YVn0'
                           'oA.WT_USo8F4bTkxwenEGx0DU0ZzwQ'}
