from os import name
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

PATH = "/usr/bin/chromedriver"
s=Service(PATH)
driver=webdriver.Chrome(service=s)
driver.get("https://orteil.dashnet.org/cookieclicker/")

element = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.ID, "langSelect-EN")))
element = driver.find_element(By.ID, "langSelect-EN")
element.click()

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies")
prices=["productPrice" + str(i) for i in range(1, -1, -1)]
items = [driver.find_element(By.ID, i) for i in prices]
actions = ActionChains(driver)
actions.click(cookie)

for i in range(5000):
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)
        print(value)
        if value <=count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.click(item)
            upgrade_actions.perform()


