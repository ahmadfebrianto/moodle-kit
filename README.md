# moodle-kit
A small Python package with some functionalities to deal with moodle-based LMS.


## Installation

```python
# New installation
pip3 install moodle-kit
```
or

```python
# Upgrade installation
pip3 install moodle-kit --upgrade
```

## Usage

```python
# Import Moodle class from package
from moodle_kit import Moodle

# Instantiate an object from Moodle class
moodle = Moodle()
```

## Available features

* Login 
```python
login_url = 'https://example.com/login/index.php'
username = 'your_username'
password = 'your_password'

moodle.login(login_url, username, password)

# The response object is automatically saved in moodle.response property. 
print(moodle.response.status_code)

# However, you can also assign a varible to it.
response = moodle.login(login_url, username, password)
print(moodle.response.status_code)
```

* Logout
```python
moodle.logout()

# After logging out, the moodle.response property is updated. So, you can verify if it's successful or not by printing the url.
print(moodle.response.url)
```
