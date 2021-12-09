from selenium import webdriver
import unittest
import time
import sys
sys.path.append("..")
import BaseTest
import pages.search_page

class serachtest(unittest.TestCase):
    def setUp(self):       
        self.test = BaseTest.BaseTest()
        self.driver = self.test.start_test()
        self.driver.implicitly_wait(50)
        self.driver.get("https://www.google.com")

    def test_google_search(self):          
        searchpage = pages.search_page.searchpage(self.driver)                
        searchpage.fill_search_text('automation')
        time.sleep(2)
        searchpage.click_search()               
        time.sleep(5)
        
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
