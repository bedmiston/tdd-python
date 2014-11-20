from selenium import webdriver

browser = webdriver.Firefox()
browser.get('http://33.33.33.33')

assert 'Django' in browser.title
