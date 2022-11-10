from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
Driver.maximize_window()
act=ActionChains(Driver)
Source_ele=Driver.find_element(By.ID,"box3")
Target_ele=Driver.find_element(By.ID,"box103")



act.drag_and_drop(Source_ele,Target_ele).perform()  #drag and drop action



# another example of drag and drop



