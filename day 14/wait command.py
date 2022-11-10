# for synchronization  (when script is run properly before the displaying the aplication) the application not loaded properly thats becoz. test script is fail
# to solve the synchronization problem wait command is used
# for that we use time method (time.sleep())
# wait command  their are two types = 1) implicit wait and 2) explicit wait
# time.sleep(in seconds)= advantage: simple to use
# disadvantage--> 1) performace of the script is  very poor
#                 2) when element is not available with in mentioned time , still their is chance of getting exception
#import time
#1) implicitly_wait command= 1)simple syntax.
#                   2)main advantage is this command maintain the performance issue
#                   3)we can give implicitly wait at the beginning of code(after the driver instance) , at any stage  . the synchronizhation is occure the implicit wait is handle that
# Disadvantage: when element is not available with in mentioned time , still their is chance of getting exception

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)
Driver.implicitly_wait(10) # in sec. we can increase any no. of sec # but maximum std. is 10 sec.

Driver.get("https://www.google.com/")

sendbox=Driver.find_element(By.NAME,'q')
sendbox.send_keys("selenium")

#time.sleep(10)
send_box=Driver.find_element(By.TAG_NAME,"svg")
send_box.click()

