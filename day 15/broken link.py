#how to handle broken link
# Broken link Doesn't have any target page
# main point all the broken link which is error code greater than 400 and normal link which is less than 400
# less than 400 error is response code and greater than 400 is error code

import requests as requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("http://www.deadlinkcity.com/")
Driver.maximize_window()

all_link=Driver.find_elements(By.TAG_NAME,"a")
Count=0
#
for link in  all_link:
  url=link.get_attribute("hrf")

  Res= requests.head("http://url?")



  if Res.status_code>=400:
   print(url, "  is a Broken link")
   Count+=1
  else:
    print(url,"  is a valis link ")

print("Total no. of Broken links:", Count)


