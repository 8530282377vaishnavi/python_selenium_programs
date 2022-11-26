from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)
Driver.get("https://accounts.google.com")
Driver.find_element(By.NAME,"identifier").send_keys("patilvv.123vgs@gmai.com")


























































