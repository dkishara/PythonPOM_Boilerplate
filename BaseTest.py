from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BaseTest(object):
    browser = None
    def __init__(self):
        print('init base test')
    def start_test(self):
        # chrome_options = Options()
        # chrome_options.add_argument("user-data-dir=selenium") 
        driver = webdriver.Chrome()
        self.browser = driver
        return driver 
    def endtest(self):
        self.browser.close()
        self.browser.quit()

