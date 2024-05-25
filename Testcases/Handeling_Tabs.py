from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.surekhatech.com/")
driver.maximize_window()
odooIcon = driver.find_element(By.XPATH,"//img[@alt='Surekhatech @ Odoo App Store']")
# Code form scrolling Down
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.execute_script("arguments[0].scrollIntoView(true);", odooIcon)
odooIcon.click()

# To get the number of windows open
numOfBrowser = (len(driver.window_handles))
print(numOfBrowser)

# TO get the name of all windows
winndowsName = driver.window_handles
print(winndowsName)

# To get the name of current window
current_window = driver.current_window_handle
print(current_window)

# To give the value of 2 window first window value will be 0, this is just for getting value of window
new_Tab = driver.window_handles[1]

if current_window !=new_Tab:
    # This method is user to switch the window swithch to and the value should be in string only
    driver.switch_to.window(new_Tab)
    print(driver.current_window_handle)

searchTab = driver.find_element(By.XPATH, "//input[@name='search']")
searchTab.send_keys("Test")

driver.switch_to.window(current_window)
print(driver.current_window_handle)

driver.switch_to.new_window()
print(driver.current_window_handle)

input("e")

