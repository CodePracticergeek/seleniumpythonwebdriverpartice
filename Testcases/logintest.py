from selenium import webdriver
from selenium.webdriver.common.by import By
from POM.LoginXpath import *
from POM.MainPage import *


driver = webdriver.Chrome()

# To Open the URL
driver.get(login_url)

# To Maximize the window
driver.maximize_window()

# To Enter the User ID and Password
user = driver.find_element(By.XPATH, xpath_username)
password1 = driver.find_element(By.XPATH, xpath_password)
user.send_keys(user_name)
password1.send_keys(password)

# To click on the Login Button
click_button = driver.find_element(By.ID, login_button)
assert not click_button. get_attribute("enable")
click_button.click()
sucess_element = driver.find_element(By.XPATH,Title_Xpath)
assert sucess_element.text == "Products"


#To check the Actual URL and Expected URL after Login
actual_url = driver.current_url
if expected_url == actual_url:
    print("User ID and Password is correct")
else:
    print("Incorrect user Id and Password")

# To move backward
driver.back()
driver.implicitly_wait(100)
driver.forward()
driver.implicitly_wait(100)
driver.refresh()
print("This is done")

try:
    for width, height in viewport:
        driver.set_window_size(width, height)
finally:
    cur_utl = driver.current_url
    print(cur_utl)
