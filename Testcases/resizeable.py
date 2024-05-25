from  selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://demo.automationtesting.in/Resizable.html"

# To get the url
driver.get(url)

# To maximize the window
driver.maximize_window()

scroll_down = driver.find_element(By.XPATH, '//*[@id="header"]/nav/div/div[2]/ul/li[3]/a')
driver.execute_script("arguments[0].scrollIntoView(true);",scroll_down)


resiabzable = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
IntialSize = driver.find_element(By.XPATH, '//*[@id="resizable"]')
initialSzieofFrmae = IntialSize.size
print(initialSzieofFrmae)


actions = ActionChains(driver)
actions.click_and_hold(resiabzable).move_by_offset(200, 200).release().perform()
Newframesize = IntialSize.size
print(Newframesize)