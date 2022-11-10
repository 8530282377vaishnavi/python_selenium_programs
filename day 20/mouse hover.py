from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://nrcp.icar.gov.in/")
Driver.maximize_window()

Home=Driver.find_element(By.XPATH,"//a[normalize-space()='Home']")
Overview=Driver.find_element(By.XPATH,"//a[normalize-space()='Overview']")
Mandate=Driver.find_element(By.XPATH,"//a[normalize-space()='Mandates']")

act=ActionChains(Driver)
#Create an action=.click(),  for perform =click().perform
act.move_to_element(Home).move_to_element(Overview).move_to_element(Mandate).click().perform()
#


