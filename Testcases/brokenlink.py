import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/")
driver.maximize_window()
urls = driver.find_elements(By.TAG_NAME, "a")
print(f"Total URLs are: {len(urls)}")

for links in urls:
    href = links.get_attribute('href')
    respone = requests.get(href)
    if respone.status_code >=400:
        print(f"Broker link:{href}(staus code:{respone.status_code}")
driver.quit()

