from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = "https://the-internet.herokuapp.com/iframe"
driver.get(url)

driver.maximize_window()
# To get the value of Iframe
iframe = driver.find_element(By.ID, "mce_0_ifr")

# To switch to the Iframe
driver.switch_to.frame(iframe)
insideIframe = driver.find_element(By.ID, "tinymce")
print("This is sucessfull")

textInsideFrame = insideIframe.text
print(textInsideFrame)

# To switch to the main section again
driver.switch_to.default_content()
driver.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').click()

#  To get the total number of window
totalWindows = driver.window_handles
print(len(totalWindows))
print(driver.window_handles)

# To get the current window value
currentWindow = driver.current_window_handle
print(currentWindow)

# To get the new wondow value
new_wind = driver.window_handles[1]
print(new_wind)

# To check the currenrt window is not teh new window the switch to new window
if new_wind!=currentWindow:
    driver.switch_to.window(new_wind)

# To get the new window value
currentUrl = driver.current_url
print(currentUrl)

# To click on the dropw down under the new window
drop_down = driver.find_element(By.XPATH, "//select[@id='options']")
driver.execute_script("arguments[0].scrollIntoView(true)", drop_down)
drop_down.click()

#  To get all the option under the drop down and then with len get the number of options
select = Select(drop_down)
select.select_by_visible_text("Python")
allOPtion = select.options
print(len(allOPtion))
value = "Ruby"

#  To find the specify option as Ruby from the dropdown and select the same and print the value for same
for options in allOPtion:
    allvalue = options.text
    if allvalue == value:
        print("Found the language", allvalue)
        select.select_by_visible_text(allvalue)
        text = select.first_selected_option
        print(text.text)

# To again switch to the old window
driver.switch_to.window(currentWindow)
newUrl2 = driver.current_url
print(newUrl2)

