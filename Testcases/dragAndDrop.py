from  selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/javascript_alerts"

driver.get(url)
driver.maximize_window()

sourcePlace = driver.find_element(By.ID, "column-a")
destinationPlace = driver.find_element(By.ID, "column-b")
actions = ActionChains(driver)
actions.drag_and_drop_by_offset(sourcePlace,destinationPlace)
actions.perform()
