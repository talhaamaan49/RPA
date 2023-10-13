import streamlit as sl

sl.set_page_config(page_title="Amaan",layout='centered')
sl.title("Robotic Process Automation")

def rpa():
    # create a driver object using driver_path as a parameter
    #driver = webdriver.Chrome(service = Service(executable_path=driver_path))
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    
    # import from webdriver_manager (using underscore)
    from webdriver_manager.chrome import ChromeDriverManager 
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    web = 'https://www.google.com/'
    driver.get(web)

    # # import more
    from selenium.webdriver.common.by import By
    # # assign any keyword for searching
    keyword = "amazon"
    # # create WebElement for a search box
    search_box = driver.find_element(By.ID, 'APjFqb')
    # # type the keyword in searchbox
    search_box.send_keys(keyword)
    search_box.submit()

    # # create WebElement for a search button
    search_amazon = driver.find_element(By.CLASS_NAME, 'VuuXrf')
    search_amazon.click()
    

    mobile = user_input1
    search_mobile = driver.find_element(By.ID, 'twotabsearchtextbox')
    
    search_mobile.send_keys(mobile)
    search_mobile.submit()

    search_amazon = driver.find_element(By.CLASS_NAME,'s-image')
    search_amazon.click()
    
user_input1 = sl.text_input('Enter the product')
btn = sl.button('Submit')
if btn:
    rpa()
 
