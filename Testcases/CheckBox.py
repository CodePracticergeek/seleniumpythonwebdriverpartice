from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.common.keys import *


driver = webdriver.Chrome()

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()
driver.refresh()


# Scroll down the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Scroll To a Specific page
scroll_element = driver.find_element(By.XPATH, "//div[@id='q15']")
driver.execute_script("arguments[0].scrollIntoView(true);", scroll_element)


checkbox = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkboxes in checkbox:
    #checkboxes.send_keys(Keys.SPACE)
    driver.execute_script("arguments[0].click();", checkboxes)
count_checkbox = 0
expected_count = 9
for checkboxes in checkbox:
    if checkboxes.is_selected():
       count_checkbox +=1

if expected_count ==count_checkbox:
    print("All are checked", count_checkbox)
else:
    print("All are not checked", count_checkbox)




# Keep the browser open until user input
input("Press Enter to close the browser...")