NEGATIVE_LOGIN_CREDENTIALS = [
   ("", "!QAZ2wsx"),
   ("qa_test@test.ru", ""),
   ("qa_test", "!QAZ2wsx"),
   ("test@test.ru", "1QAZ2wsx")
]


POSITIVE_LOGIN_CREDENTIALS = {"email": "qa_test@test.ru",
                             "password": "!QAZ2wsx"}


class Links:
   base_url = "https://qastand.valhalla.pw/"
   login = base_url + "login"
   profile = base_url + "profile"
   blog = base_url + "blog"


SESSION_COOKIE = {'name': 'session',
                 'value': '.eJwlzjsOwjAMANC7ZGawHX-SXqaKY0ewtnRC3J1KTG99n7KvI89n2d7HlY-yv6JsBaMOY1RaQNzqSp05QsSpazaXI'                  'FATqiOH1qnCbI3SQRHSAmG26k1o9NWhMknrWN37jU0IU45wme5GiyWBHLkj8mzc09y03JHrzOO_ofL9AVk6Le8.YVn0'
'oA.WT_USo8F4bTkxwenEGx0DU0ZzwQ'}

