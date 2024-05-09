import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url="https://topis.seoul.go.kr/"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(url)
driver.implicitly_wait(0.5)


search_input=driver.find_element(By.ID,"searchTxt")
ActionChains(driver).send_keys_to_element(search_input,"화곡").perform()
time.sleep(10)