#alert messages

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Firefox()
driver.get("https://demoqa.com/alerts")
driver.maximize_window()
wait =WebDriverWait(driver,10)

alert=wait.until(EC.element_to_be_clickable((By.ID,"alertButton")))
alert.click()

alert=driver.switch_to.alert
time.sleep(2)
print(alert.text)
alert.accept()

confirm_id=wait.until(EC.element_to_be_clickable((By.ID,"timerAlertButton")))
confirm_id.click()
time.sleep(6)

alert1=driver.switch_to.alert
time.sleep(2)
print(alert1.text)
alert1.accept()

confirm_box=wait.until(EC.element_to_be_clickable((By.ID,"confirmButton")))
confirm_box.click()
time.sleep(2)

alert2=driver.switch_to.alert
time.sleep(2)
print(alert2.text)
alert2.dismiss()

prompt=wait.until(EC.element_to_be_clickable((By.ID,"promtButton")))
prompt.click()

alert3=driver.switch_to.alert
print(alert3.text)
alert3.send_keys("Pramod")
time.sleep(2)
alert3.accept()

