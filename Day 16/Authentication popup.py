# authentication popup
#concept of injection = bypass by injecting the username and password
# their is no need find_element=Diretly in  url we can metion the text(username and password)-->http://username:password@test.com
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.by import By
serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

# Bypass thrrough automation
Driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
Driver.maximize_window()
