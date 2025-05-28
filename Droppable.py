from selenium import webdriver
from selenium.webdriver.common.by import By



driver=webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
driver.implicitly_wait(10)

subject=driver.find_element(By.XPATH,"//input[@id='subjectsInput']")
subject.click()

subject.send_keys("Ch")

subject_option=driver.find_element(By.XPATH,"//div[text()='Chemistry']")
subject_option.click()
