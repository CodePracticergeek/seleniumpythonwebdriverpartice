import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()
images = driver.find_elements(By.TAG_NAME, "img")
brokenImages = []
NotbrokernImages =[]
for image in images:
    src = image.get_attribute("src")
    code = requests.get(src)
    # Status code is an inbuild functonality where we get the status of the Source
    # In this our source is SEC udner Image Tag and we will get the status of that
    get = code.status_code
    if get !=200:
        print("Is a brokern images")
        brokenImages.append(src)
    else:
        print("Not an Broken images")
        NotbrokernImages.append(src)

    # Have store all the broken link under Array BrokenImages
for brokenImage in brokenImages, NotbrokernImages:
    if  brokenImage:
        print("This are the broken images", brokenImage)
    else:
        print("Not an broken images", NotbrokernImages)
