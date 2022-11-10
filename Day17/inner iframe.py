from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

# Bypass thrrough automation
Driver.get("https://demo.automationtesting.in/Frames.html")
Driver.maximize_window()

Driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()

outerframe=Driver.find_element(By.XPATH,"//a[@class='analystic']").click()
Driver.switch_to.frame(outerframe)



innerframe=Driver.find_element(By.XPATH,'/html/body/section/div/div').click()
Driver.switch_to.frame(innerframe)

Driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("WELCOME")

Driver.switch_to.parent_frame()

