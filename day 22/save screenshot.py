# how to save screen shot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get('https://demo.nopcommerce.com/')
Driver.maximize_window()

Driver.save_screenshot(os.getcwd()+"//hompage.png")
Driver.get_screenshot_as_file()
#Driver.get_screenshot_as_png()   #Driver.get_screenshot_as_base64()  #In binary format save the screen shot



