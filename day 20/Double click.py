from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
Driver.maximize_window()


Driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")