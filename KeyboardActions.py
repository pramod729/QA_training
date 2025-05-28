#Keyboard actions

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium .webdriver.common.action_chains import ActionChains


driver=webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

actions=ActionChains(driver)
firstname=driver.find_element(By.ID,"firstName")
actions.click(firstname).send_keys("Pramod"+Keys.TAB).perform()

lastname=driver.find_element(By.ID,"lastName")
actions.click(lastname).send_keys("Aryal"+Keys.TAB).perform()

email=driver.find_element(By.ID,"userEmail")
actions.click(email).send_keys("aryalpramod22@gmail.com"+Keys.TAB).perform()

gender=driver.find_element(By.ID,"gender-radio-1")
actions.click(gender).perform()

phone = driver.find_element(By.ID, "userNumber")
actions.click(phone).send_keys("9874561230"+Keys.TAB).perform()

# dateofbirth=driver.find_element(By.ID,"dateOfBirthInput")
# actions.click(dateofbirth)
# month=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']")
# actions.click(month)
# monthvalue=driver.find_element(By.XPATH,"//select[@class='react-datepicker__month-select']/option[1]")
# actions.click(monthvalue)
# year=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']")
# actions.click(year)
# yearvalue=driver.find_element(By.XPATH,"//select[@class='react-datepicker__year-select']/option[3]")
# actions.click(yearvalue)
# date=driver.find_element(By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='7' and not(contains(@class, 'outside-month'))]")
# actions.click(date)


hobbies=driver.find_element(By.ID,"hobbies-checkbox-1")
actions.click(hobbies).perform()
time.sleep(2)

address=driver.find_element(By.XPATH,"//textarea[@id='currentAddress']")
actions.click(address).send_keys("Lolang", Keys.TAB).perform()


# State_ =driver.find_element(By.XPATH,"//div[text()='Select State']")
# actions.click(State_).send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAB).perform()
# actions.click(State_)

# city_dropdown = driver.find_element(By.XPATH, "//div[text()='Select City']")
# actions.click(city_dropdown).send_keys(Keys.ARROW_DOWN).send_keys(Keys.TAAB).perform()
# actions.click(city_dropdown)

# submit=driver.find_element(By.ID,"submit")
# actions.click(submit)
