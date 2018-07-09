# Python unit testing framework
import unittest
# Appium Python client
from appium import webdriver

# Open iOS simulator 11.2 and install TestApp
capabilities = {
  'platformName': 'iOS',
  'platformVersion': '11.4',
  'browserName': 'Safari',
  'deviceName': 'iPhone 8'
}

# setup the web driver and launch the webview app.
#capabilities = { 'browserName': 'Safari'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

# Navigate to the page and interact with the elements on the guinea-pig page using id.
driver.get('https://dog.ceo/dog-api/');
#div = driver.find_element_by_id('i_am_an_id')
# check the text retrieved matches expected value
#assertEqual('I am a div', div.text)

# populate the comments field by id
#driver.find_element_by_id('comments').send_keys('My comment')

# close the driver
driver.quit()