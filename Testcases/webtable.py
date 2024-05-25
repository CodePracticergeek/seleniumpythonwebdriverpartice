from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://cosmocode.io/automation-practice-webtable/"
driver.get(url)
driver.maximize_window()

# To scroll down to the tabel
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
table = driver.find_element(By.ID, "countries")
driver.execute_script("arguments[0].scrollIntoView(true);", table)

# To get the total number of Rows in number. In rows we will nor get the cell value
rows = table.find_elements(By.TAG_NAME, "tr")
row_count = len(rows)
print(row_count)
targetValue = "Indias"
found = False
for row in rows:
    # To get the total number of cells and to get the text of the cell we user cell.text methof
    cells = row.find_elements(By.TAG_NAME, "td")
    for cell in cells:
        if targetValue == cell.text:
            print("Found the value", targetValue)
            found =True
            break
    if found:
        break
if not found:
    print("Didn't find the value", targetValue)

