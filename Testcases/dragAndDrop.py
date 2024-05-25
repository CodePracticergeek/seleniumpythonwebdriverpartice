from  selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/drag_and_drop"

driver.get(url)
driver.maximize_window()

sourcePlace = driver.find_element(By.ID, "column-a")
destinationPlace = driver.find_element(By.ID, "column-b")
actions = ActionChains(driver)
actions.drag_and_drop(sourcePlace,destinationPlace)
actions.perform()
