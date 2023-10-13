import streamlit as sl
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

sl.set_page_config(page_title="Amaan", layout='centered')
sl.title("Robotic Process Automation")

def rpa():
    # create a driver object using driver_path as a parameter
    driver_path = "C:\\Users\\talha\\.wdm\\drivers\\chromedriver\\win64\\117.0.5938.134\\chromedriver-win32\\chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)

    web = 'https://www.google.com/'
    driver.get(web)

    keyword = "amazon"
    search_box = driver.find_element(By.ID, 'APjFqb')
    search_box.send_keys(keyword)
    search_box.submit()

    search_amazon = driver.find_element(By.CLASS_NAME, 'VuuXrf')
    search_amazon.click()

    mobile = user_input1  # Make sure to assign a value to this variable
    search_mobile = driver.find_element(By.ID, 'twotabsearchtextbox')
    search_mobile.send_keys(mobile)
    search_mobile.submit()

    search_amazon = driver.find_element(By.CLASS_NAME, 's-image')
    search_amazon.click()


user_input1 = sl.text_input('Enter the product')
btn = sl.button('Submit')

if btn:
    rpa()