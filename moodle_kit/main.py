from re import search
import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Moodle:

    __headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Cookie': ''
    }
   
    __logintoken = None
    __moodle_session = None


    def __init__(self) -> None:
        pass

    
    def __get_logintoken(self, string):
        try:
            regex = r'name="logintoken".*value="(\w+)"'
            logintoken = search(regex, string).groups()[0]
            return logintoken
        except Exception:
            print("[!] Logintoken not found.")
            exit()


    def login(self, url, username, password):
        response = requests.get(
            url,
            allow_redirects=True
        )

        if response.ok:
            self.__logintoken = self.__get_logintoken(response.text)
            self.__moodle_session = response.cookies.get('MoodleSession')
            self.__headers['Cookie'] = "MoodleSession=" + self.__moodle_session
        else:
            print("[!] Couldn't reach the website.")
            exit()

        response = requests.post(
            url,
            headers=self.__headers,
            data={
                'anchor': '',
                'logintoken': self.__logintoken,
                'username': username,
                'password': password
            },
            allow_redirects=True
        )

        new_moodle_session = response.request.headers.get('Cookie').split('=')[1]
        self.__headers['Cookie'] = 'MoodleSession=' + new_moodle_session
        return response

    
    def logout(sself):
        pass



