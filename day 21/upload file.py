from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)
Driver.implicitly_wait(10)

Driver.get("https://www.monsterindia.com/seeker/registration")
Driver.maximize_window()
Driver.find_element(By.XPATH,"//span[@class='browse-text']").click()
Driver.find_element(By.XPATH,"//input[@id='file-upload']").send_keys("C:\Vaishnavi Patil(1)")