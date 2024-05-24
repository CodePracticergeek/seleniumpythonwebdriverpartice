from selenium import webdriver

driver = webdriver.Chrome


# Variabales
Title_Xpath = "//*[@id='inventory_filter_container']/div"
viewport = [(1284, 785),(796, 1285), (643, 788)]

# methods

def page_size(X, Y):
    try:
        for width,height in viewport:
            driver.set_window_size(width, height)
    finally:
        cur_utl = driver.current_url
        print(cur_utl)
