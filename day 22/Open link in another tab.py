# i want to open link on new tab
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

# Driver.get('https://demo.nopcommerce.com/')
# Driver.maximize_window()
# Reglink=Keys.CONTROL+Keys.RETURN
# Driver.find_element(By.LINK_TEXT,"Register").send_keys(Reglink)



## tab open : in selenium4 == using switch to new window
# Driver.get("https://demo.nopcommerce.com/")
# Driver.switch_to.new_window()
# Driver.get("https://opensource-demo.orangehrmlive.com/")

## tab open : in selenium4 == using switch to new Browser
Driver.get("https://demo.nopcommerce.com/")
Driver.switch_to.new_window("window")
Driver.get("https://opensource-demo.orangehrmlive.com/")

