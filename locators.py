from calendar import month
from multiprocessing.connection import address_type
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.action_chains import ActionChains
import time

driver=webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

firstname=driver.find_element(By.ID,"firstName")
firstname.send_keys("Pramod ")

lastname=driver.find_element(By.ID,"lastName")
lastname.send_keys("Aryal")



gender=driver.find_element(By.ID,"gender-radio-1")
driver.execute_script("arguments[0].click()",gender)

dateofbirth=driver.find_element(By.ID,"dateOfBirthInput")
dateofbirth.click()
month=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
month.click()
monthvalue=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']/option[1]")
monthvalue.click()
year=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
year.click()
yearvalue=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']/option[3]")
yearvalue.click()
date=driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='7' and not(contains(@class, 'outside-month'))]")
date.click()


imageupload=driver.find_element(By.XPATH,"//input[@type='file']")
imageupload.send_keys(r"C:\Users\Lenovo\PycharmProjects\PythonProject\abc.jpg")

address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
address.send_keys("Lolang")

submit=driver.find_element(By.ID,"submit")
submit.click()

