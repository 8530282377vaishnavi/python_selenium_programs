# EXPLICIT WAIT= advantage=

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)
#poll_frequency=help to improve expicit_wait faster

Driver.get("https://www.google.com/")
mylist=WebDriverWait(Driver,10).until(EC.visibility_of_element_located((By.NAME,'q')))
mylist.send_keys("selenium")
# sendbox=Driver.find_element(By.NAME,'q')
# sendbox.send_keys("selenium")

#time.sleep(10)
search_link=WebDriverWait(Driver,10).until(EC.presence_of_element_located((By.XPATH,'//span[@class="QCzoEc z1asCe MZy1Rb"]')))
# send_box.click()
search_link.click()
