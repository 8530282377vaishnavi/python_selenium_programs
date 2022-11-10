#import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://testautomationpractice.blogspot.com/")
Driver.maximize_window()

Driver.find_element(By.ID,"Wikipedia1_wikipedia-search-input").send_keys("selenium")
Driver.find_element(By.XPATH,"//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").click()

# Driver.find_element(By.XPATH,"//*[@id='HTML9']/div[1]/button").click()
# time.sleep(1)
# myalert=Driver.switch_to.alert
# print(myalert.text)
# #myalert.accept()
# myalert.dismiss()


Driver.find_element(By.LINK_TEXT,"More »").click()
# Driver.find_element(By.LINK_TEXT,"Selenium in biology").click()
# Driver.find_element(By.LINK_TEXT,"Selenium (software)").click()

windowIds=Driver.window_handles

for win in windowIds:
    Driver.switch_to.window(win)
    print(Driver.title)


