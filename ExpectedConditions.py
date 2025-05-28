#implementation of EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import Keys
import os

driver = webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()
wait =WebDriverWait(driver,10)

first_name =wait.until(EC.presence_of_element_located((By.ID ,"firstName")))
first_name.send_keys("Pramod")

last_name =wait.until(EC.presence_of_element_located((By.ID,"lastName")))
last_name.send_keys("Aryal")

email =wait.until(EC.presence_of_element_located((By.ID,"userEmail")))
email.send_keys("aryalpramod22@gmail.com")

gender = wait.until(EC.element_to_be_clickable((By.XPATH,"//label[text()='Male']")))
gender.click()

number = wait.until(presence_of_element_located((By.ID,"userNumber")))
number.send_keys("9843025897")

subjects = wait.until(EC.presence_of_element_located((By.ID, "subjectsInput")))
subjects.send_keys("Maths")
subjects.send_keys(Keys.ENTER)


dob = wait.until(EC.element_to_be_clickable((By.ID, "dateOfBirthInput")))
dob.click()
month_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__month-select")))
Select(month_dropdown).select_by_visible_text("August")
year_dropdown= wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "react-datepicker__year-select")))
Select(year_dropdown).select_by_visible_text("1999")
day = driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='28' and not(contains(@class, 'outside-month'))]")
day.click()

hobby = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Sports']")))
hobby.click()

address = wait.until(EC.presence_of_element_located((By.ID, "currentAddress")))
address.send_keys("Lolang")

state = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
state.send_keys("NCR")
state.send_keys(Keys.ENTER)

state_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']")))
state_option.click()

city_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Gurgaon']")))
city_option.click()

# submit=wait.until(EC.text_to_be_present_in_element((By.ID, "submit")))
# submit.click()