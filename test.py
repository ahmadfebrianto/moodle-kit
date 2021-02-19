from bs4 import BeautifulSoup
from moodle_kit import Moodle

url = ""
username = ""
password = ""


moodle = Moodle()
response = moodle.login(url, username, password)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
