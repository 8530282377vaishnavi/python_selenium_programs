# how to handle notification popup  Notification pop up

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
ops=webdriver.ChromeOptions()
ops.add_argument("--enable-notification")
serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object,options=ops)

Driver.get("https://ultimateqa.com/dummy-automation-websites/")
Driver.maximize_window()


