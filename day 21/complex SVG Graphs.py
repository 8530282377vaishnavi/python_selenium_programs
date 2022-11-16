#

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)
Driver.get("https://emicalculator.net/")
Driver.implicitly_wait(500)
vertical_XPATH="//*[local-name()='svg']//*[name()='g' and @class='highcharts-series-group']//*[name()='rect']"
textXPATH="//*[local-name()='svg']//*[name()='g' and @class='highcharts-label highcharts-tooltip highcharts-color-undefined']//*[name()='text']"
List=Driver.find_elements(By.XPATH,vertical_XPATH)
print("total bars are:",len(List))
action=ActionChains(Driver)
for e in List:
    action.move_to_element(e).perform()
    text1=Driver.find_element(By.XPATH,textXPATH).text
    print(text1)



