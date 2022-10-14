from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"


class BasePage(object):
    def __init__(self, driver):
        self.driver=driver


class MainPage(BasePage):

    search_text_element=SearchTextElement()

    def if_title_matches(self):
        return "Python" in self.driver.title

    
    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def click_about_button(self):
        element = self.driver.find_element(*MainPageLocators.ABOUT)
        element.click()       

class SearchResultPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source

    def no_results_found(self):
        return "No results found." in self.driver.page_source

class AboutPage(BasePage):

    def if_title_matches(self):
        return "About" in self.driver.title