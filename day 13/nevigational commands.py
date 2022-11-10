# nevigational commands
# access through driver
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("https://www.snapdeal.com/")
Driver.get("https://www.amazon.in/")

Driver.back()
Driver.forward()
Driver.refresh()

time.sleep(5)

Driver.quit()
