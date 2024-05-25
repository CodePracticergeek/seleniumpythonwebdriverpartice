from  selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://the-internet.herokuapp.com/horizontal_slider"

driver.get(url)
driver.maximize_window()

slider = driver.find_element(By.XPATH, "//input[@type='range']")
actions = ActionChains(driver)
actions.click_and_hold(slider).move_by_offset(50, 0).release().perform()
