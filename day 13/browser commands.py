#two main browser commands are  close()= 1) when we use close command it will close the browser
#                                              but process is keeps running
#                                        2) close command close only one browser at a time
#                                       3) close single browser window at a time(when browser is focused )
#                               quit()=  1)when we use quit command it will close all the browser and also process will be stop
#                                        2) when we use quit command their are many opened browser close at a time
#                                        3) internaly killing the driver  process of chrome browser
# access through driver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")

Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://demo.nopcommerce.com/")

Driver.find_element(By.PARTIAL_LINK_TEXT,"nopCommerce").click()

time.sleep(4)

#Driver.close()
Driver.quit()



