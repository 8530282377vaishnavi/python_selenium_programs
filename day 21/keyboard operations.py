import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)
Driver.implicitly_wait(10)

Driver.get("https://text-compare.com/")
Driver.maximize_window()


input1=Driver.find_element(By.XPATH,"//textarea[@id='inputText1']")
input2=Driver.find_element(By.XPATH,"//textarea[@id='inputText2']")
input1.send_keys("Welcome in my world of python")

act=ActionChains(Driver)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(3)
act.send_keys(Keys.TAB).perform()
time.sleep(3)
act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()


