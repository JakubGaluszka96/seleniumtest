from selenium.webdriver.common.by import By

class MainPageLocators(object):
    GO_BUTTON = (By.ID, "submit")
    ABOUT = (By.LINK_TEXT, "About")

class SearchResultsPageLocators(object):
    pass