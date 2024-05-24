from selenium import webdriver
from selenium.webdriver.common.by import *
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()

drop_down_field = driver.find_element(By.ID, "dropdown")
select = Select(drop_down_field)

# Select. option will give the count of the
options_length = len(select.options)
print(options_length)
expected_option = 3
if expected_option==options_length:
    print("Test cases Passed")
else:
    print("Test cases fail")

# Select By Visibale Text
#Sekect By Value
#select.select_by_value("2")
#select By Index
#select.select_by_index(1)

# To check the options in the drop down and break when the option is found

target_value = "Option 1"
for option in select.options:
    if option.text == target_value:
        print(f"Value is {target_value}")
        break
    else:
        print(f"value  {target_value} not found")

for option in select.options:
    select.select_by_visible_text(option.text)
    print("All option was selected")

