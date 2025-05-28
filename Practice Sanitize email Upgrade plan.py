#sanitize email

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

upgrade_plan=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Upgrade Plan']")))
upgrade_plan.click()
time.sleep(1)

upgrade_to_pro=wait.until(EC.presence_of_element_located((By.XPATH,"(//button[text()='Upgrade to '])[1]")))
upgrade_to_pro.click()
time.sleep(1)

upgrade=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Upgrade']")))
upgrade.click()
time.sleep(1)

driver.switch_to.frame("paddle_frame")

checkbox=wait.until(EC.presence_of_element_located((By.XPATH,"//div[contains(@class,'checkbox')]")))
checkbox.click()
time.sleep(1)

Continue=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Continue']")))
Continue.click()
time.sleep(1)

Cardnumber=wait.until(EC.presence_of_element_located((By.ID,"cardNumber")))
Cardnumber.send_keys("4242424242424242")
time.sleep(1)

Name_on_card=wait.until(EC.presence_of_element_located((By.ID,"cardHolder")))
Name_on_card.send_keys("Jiwan")
time.sleep(1)

Expiration_date=wait.until(EC.presence_of_element_located((By.ID,"expiry")))
Expiration_date.send_keys("0428")
time.sleep(1)

Security_code=wait.until(EC.presence_of_element_located((By.ID,"cvv")))
Security_code.send_keys("123")
time.sleep(1)

Subscribe_now=wait.until(EC.presence_of_element_located((By.XPATH,"//button[text()='Subscribe now']")))
Subscribe_now.click()
time.sleep(1)