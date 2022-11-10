from selenium import webdriver
from selenium.webdriver.common.by import By
import os
# give a current directory location
location=os.getcwd()


def Chrome_setup():
    from selenium.webdriver.chrome.service import Service
    serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
    # Download the file in desired location
    preferances={"download.default_directory" : location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferances)
    Driver=webdriver.Chrome(service=serv_obj, options=ops)
    return Driver

Driver=Chrome_setup()
Driver.get("https://file-examples.com/index.php/sample-documents-download/")
Driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[3]/a").click()



def Edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service("C:\Driver\edgedriver_win64\msedgedriver.exe")
    # Download the file in desired location
    preferances={"download.default_directory": location}
    ops=webdriver.ChromeOptions()
    ops.add_experimental_option("prefs",preferances)
    Driver=webdriver.Edge(service=serv_obj, options=ops)
    return Driver

Driver=Edge_setup()
Driver.get("https://file-examples.com/index.php/sample-documents-download/")
Driver.find_element(By.XPATH,"//*[@id='table-files']/tbody/tr[1]/td[3]/a").click()