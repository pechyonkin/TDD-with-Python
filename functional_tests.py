# selenium allows to control a browser
from selenium import webdriver

# create a browser object
browser = webdriver.Firefox()

# open a webpage at localhost
browser.get('http://localhost:8000')

# check the title
assert 'Django' in browser.title