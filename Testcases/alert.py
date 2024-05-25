import time

from  selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/javascript_alerts"

# To get the url
driver.get(url)

# To maximize the window
driver.maximize_window()

# To click the Js Alert Icon
jsAlert = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/button')
jsAlert.click()

# To swith to the Alert
switchToAlert = driver.switch_to.alert

# To get the text of alert

textofAlert = switchToAlert.text
print(textofAlert)

# To accept the alert
switchToAlert.accept()

# To get the second Alert
jsConfrim = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
jsConfrim.click()

# To switch to the js confirm alert
jsConfrimAlert = driver.switch_to.alert

# To get the text of the alert
textofJSDismissAlert =jsConfrimAlert.text
print(textofJSDismissAlert)

# To dissmiss the alert
jsConfrimAlert.dismiss()

# To click on the 3 alert
jsPromot = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[3]/button')
jsPromot.click()

# To switch to JS Promot ALert Box
jsPromotSwitch =driver.switch_to.alert

# To get the text
textofJSPromto = jsPromotSwitch.text
print(textofJSPromto)

# To type udner the alert box
jsPromotSwitch.send_keys("Hello Sir")

time.sleep(10)

# To accept the alert
jsPromotSwitch.accept()

