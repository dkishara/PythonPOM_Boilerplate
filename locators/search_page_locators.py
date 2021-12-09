import sys
sys.path.append("..")

from selenium.webdriver.common.by import By

class searchpagelocators():
    SEARCH_TEXT = (By.NAME,'q')  
    SEARCH_BUTTON = (By.NAME,'btnK')

  