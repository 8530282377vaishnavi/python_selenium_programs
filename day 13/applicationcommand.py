# application command access through driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")

Driver=webdriver.Chrome(service=serv_obj)

#application related commands =get(),title,currunt_page,page_source
Driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")  # opening the page of the url


print(Driver.title) # to capture the title of the page
print(Driver.current_url) # to capture currunt url of the page
print(Driver.page_source) # to capture th source code of the page


