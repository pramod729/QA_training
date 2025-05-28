import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://training.rcvacademy.com/test-automation-practice-page")

Dropdown=Select(driver.find_element(By.XPATH,"//select[contains(@class,'form-control zen-custom-elm')]"))
Dropdown.select_by_visible_text("Amazon")
time.sleep(2)


