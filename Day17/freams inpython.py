#frames, iframes, form  these three are same
# IN THE FRAMES there are switch_to.frame(name),switch_to.frame(ID),switch_to.frame(web-element),switch_to.frame(0)




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

# Bypass thrrough automation
Driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
Driver.maximize_window()

Driver.switch_to.frame("packageListFrame")
Driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()
Driver.switch_to.default_content() # this is help 


Driver.switch_to.frame("packageFrame")
Driver.find_element(By.LINK_TEXT,"WebDriver").click()
Driver.switch_to.default_content()

Driver.switch_to.frame("classFrame")
Driver.find_element(By.XPATH,"/html/body/header/nav/div[1]/div[1]/ul/li[8]/a").click()
