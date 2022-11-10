#alert window / popup--> this not a webelement
# import time
#
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
#
#
# serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
# Driver=webdriver.Chrome(service=serv_obj)
# Driver.get("http://the-internet.herokuapp.com/javascript_alerts")
# Driver.maximize_window()
# Driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
#
# time.sleep(5)
#
# alertwindow=Driver.switch_to.alert
# print(alertwindow.text)
# alertwindow.send_keys("Welcome")
#
# # alertwindow.accept() # close the alert window by using ok button
# alertwindow.dismiss() # close the alert window by using cancle button
# #ans shows the null


#example 2
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)
Driver.get("https://mypage.rediff.com/login/dologin")
Driver.maximize_window()
Driver.find_element(By.XPATH,"//input[@id='txtlogin']").submit()


time.sleep(5)
myalert=Driver.switch_to.alert
print(myalert.text)
myalert.accept()
Driver.close()
