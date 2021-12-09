import sys
sys.path.append("..")

from BasePage import BasePage
from locators.search_page_locators import searchpagelocators

class searchpage(BasePage): 
    def fill_search_text(self,searchtext):
         element = self.driver.find_element(*searchpagelocators.SEARCH_TEXT)
         element.clear()      
         element.send_keys(searchtext)

    def click_search(self):
        element = self.driver.find_element(*searchpagelocators.SEARCH_BUTTON)
        element.click() 