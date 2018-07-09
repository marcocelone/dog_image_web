"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from appium import webdriver as appiumdriver

class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://dog.ceo/dog-api/"
        if self.browser == "iexplorer":
            # Set ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set chrome driver
            driver = webdriver.Chrome()
        elif self.browser == "ios_mobile":
            capabilities = {
                'platformName': 'iOS',
                'platformVersion': '11.4',
                'browserName': 'Safari',
                'deviceName': 'iPhone 8'
            }
            driver = appiumdriver.Remote('http://localhost:4723/wd/hub', capabilities)
            driver.get(baseURL)

        else:
            driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        #driver.implicitly_wait(3)
        # Maximize the window
        #driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver