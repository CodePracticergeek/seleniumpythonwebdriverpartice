import time
from datetime import *

from  selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://www.globalsqa.com/demo-site/datepicker/"

# To get the url
driver.get(url)

# To maximize the window
driver.maximize_window()

# Need to close the Pop up
driver.find_element(By.XPATH, '//*[@id="post-2661"]/div[2]/div/div/div[1]/div/a').click()

# To switch to iframe first
iframe = driver.find_element(By.XPATH, '//*[@id="post-2661"]/div[2]/div/div/div[1]/p/iframe')
driver.switch_to.frame(iframe)

# Click on datepicker
datePicker = driver.find_element(By.ID, 'datepicker')
datePicker.click()

# To get the current date
currentDate = datetime.now()

# To increase or decrease the current date
nextDate = currentDate + timedelta(days=2)

# Format of date
formatedDate = nextDate.strftime("%m/%d/%Y")

# To update the date in the datepicker and select the dame by using Tab button
datePicker.send_keys(formatedDate+Keys.TAB)

# Switch out of the Iframe
driver.switch_to.default_content()
back = '//*[@id="wrapper"]/div[1]/div[1]/div/div/div/div[1]/a[2]/span'
driver.find_element(By.XPATH, back).click()
print(driver.current_url)



input("e")