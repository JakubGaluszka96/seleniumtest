import unittest
from selenium import webdriver
import page
from selenium.webdriver.chrome.service import Service


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        PATH = "/usr/bin/chromedriver"
        s=Service(PATH)
        self.driver=webdriver.Chrome(service=s)
        self.driver.get("http://www.python.org")
        

    def test_search_python(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.if_title_matches()
        mainPage.search_text_element = "pycon"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_results_found()

    def test_no_results(self):
        mainPage=page.MainPage(self.driver)
        assert mainPage.if_title_matches()
        mainPage.search_text_element = "pupupu"
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.no_results_found()


    def test_about_access(self):
        mainPage=page.MainPage(self.driver)
        mainPage.click_about_button()
        about_page = page.AboutPage(self.driver)
        assert about_page.if_title_matches()

    def tearDown(self):
        self.driver.close()


if __name__=="__main__":
    unittest.main()