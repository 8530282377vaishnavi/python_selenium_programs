# webtable
# 2) dynamic table= the size odf table is not fixed the data will be added continuously or deleted

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
Driver.maximize_window()
# Driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
# Driver.find_element(By.XPATH," //input[@placeholder='Password']").send_keys("admin123")
# Driver.find_element(By.XPATH,"//input[@placeholder='Username']").submit()

