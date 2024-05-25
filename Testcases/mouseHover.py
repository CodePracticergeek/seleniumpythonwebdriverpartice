from datetime import *

from  selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://demo.automationtesting.in/Register.html"

# To get the url
driver.get(url)

# To maximize the window
driver.maximize_window()

# Action class for hovering the mouse
actions = ActionChains(driver)
switchElement = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/a')
hovermouse = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[4]/ul/li[3]/a')

# To perform the action on the the element which is showing ElementNotInteractableException
actions.move_to_element(switchElement).perform()
hovermouse.click()