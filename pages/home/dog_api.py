from selenium.webdriver.common.by import By
from datetime import datetime
from base.selenium_driver import SeleniumDriver


class HomePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators
    _documentation = 'div.vertical-nav.ul.li:nth-child(1)'
    _breedlist = 'body > div.vertical-nav > ul > li:nth-child(2) > a'
    _shop = 'body > div.vertical-nav > ul > li:nth-child(3) > a'
    _about = 'body > div.vertical-nav > ul > li:nth-child(4) > a'
    _submit_dog = 'body > div.vertical-nav > ul > li:nth-child(5) > a'
    _side_nav_menu = 'div.vertical-nav'
    _email = 'mce-EMAIL'
    _join_button = 'mc-embedded-subscribe'
    _contact_page_title = 'Dog API'
    _success_join = 'Website'
    _email_exist_check = '#mergeRow-0'
    _fetch_button = ".body > div.api-side.home > div.code-wrapper > a"
    _fetch_image = "body > div.api-side.home > div.try > div.image > div > img"


    def verify_home_page(self):
        self.get_title(self._contact_page_title)

    def verify_sidenave_menu(self):
        self.elementPresenceCheck(self._side_nav_menu, 'css')

    def verify_side_menu_elements(self):
        self.elementPresenceCheck(self._documentation, 'css')
        self.elementPresenceCheck(self._breedlist, 'css')
        self.elementPresenceCheck(self._shop, 'css')
        self.elementPresenceCheck(self._about, 'css')
        self.elementPresenceCheck(self._submit_dog, 'css')

    def documentation_page(self):
        self.elementClick(self._documentation, locatorType='css')

    def join_new_email(self):
        date = str(datetime.now())
        self.sendKeys(date.strip()+'@test.com', self._email, locatorType="id")
        self.elementClick(self._join_button, locatorType="id")
        self.get_title(self._success_join)

    def subscribed_email(self):
        self.sendKeys('mytest@test.com', self._email, locatorType="id")
        self.elementClick(self._join_button, locatorType="id")
        self.elementPresenceCheck(self._email_exist_check, 'css')

    def fetch_button_functionality(self):
        self.elementClick(self._fetch_image, locatorType='css')
        self.elementClick(self._fetch_button, locatorType='css')
        self.elementClick(self._fetch_image, locatorType='css')
















