from re import search as re_search
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Moodle:

    request_headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Cookie': ''
    }

    response = None
    __logintoken = None
    __moodle_session = None

    def __init__(self) -> None:
        pass

    def __get_logintoken(self, string):
        try:
            regex = r'name="logintoken".*value="(\w+)"'
            logintoken = re_search(regex, string).groups()[0]
            return logintoken
        except Exception:
            print("[!] Logintoken not found.")
            exit()

    def login(self, url, username, password):
        self.response = requests.get(
            url,
            allow_redirects=True
        )

        if self.response.ok:
            self.__logintoken = self.__get_logintoken(self.response.text)
            self.__moodle_session = self.response.cookies.get('MoodleSession')
            self.request_headers['Cookie'] = "MoodleSession=" + \
                self.__moodle_session
        else:
            print("[!] Couldn't reach the website.")
            exit()

        self.response = requests.post(
            url,
            headers=self.request_headers,
            data={
                'anchor': '',
                'logintoken': self.__logintoken,
                'username': username,
                'password': password
            },
            allow_redirects=True
        )

        new_moodle_session = self.response.request.headers.get('Cookie').split('=')[
            1]
        self.request_headers['Cookie'] = 'MoodleSession=' + new_moodle_session
        return self.response

    def logout(self):
        regex = r'href="(.*logout.php\?sesskey=\w+)"\s?'
        logout_url = re_search(regex, self.response.text).groups()[0]
        self.response = requests.get(logout_url, headers=self.request_headers)
        return self.response

    @property
    def title(self):
        regex = r'<title>(.*)</title>'
        page_title = re_search(regex, self.response.text).groups()[0]
        return page_title
