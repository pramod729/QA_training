import time
from asyncio import wait_for

from pycparser.c_ast import Continue
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Firefox()
driver.get("https://sanitize-crm.netlify.app/login")
driver.maximize_window()
wait =WebDriverWait(driver,10)

email=wait.until(EC.presence_of_element_located((By.NAME,"email")))
email.send_keys("aryalpramod52@gmail.com")
time.sleep(2)

password=wait.until(EC.presence_of_element_located((By.NAME,"password")))
password.send_keys("Pramod@2580")
time.sleep(1)

remember_me=wait.until(EC.presence_of_element_located((By.XPATH,"//label[text()='Remember Me']")))
remember_me.click()
time.sleep(1)

login=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Login']")))
login.click()
time.sleep(1)

clean_list = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[text()='Clean List']")))
clean_list.click()
time.sleep(1)

start_cleaning=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Start cleaning']")))
start_cleaning.click()
time.sleep(2)

list_name=wait.until(EC.presence_of_element_located((By.NAME,"name")))
list_name.send_keys("Unverified Emails")
time.sleep(1)

file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys(r"C:\Users\Lenovo\Desktop\unverified emails.csv")
time.sleep(1)

validation_type=wait.until(EC.presence_of_element_located((By.CLASS_NAME,"select__input-container css-19bb58m")))
validation_type.click()
time.sleep(1)

clean_list1=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Clean List']")))
clean_list1.click()
time.sleep(1)

