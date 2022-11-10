#drag and drop slider with scrolling page is  apart of the mouse operations  but not a part of action chain
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
Driver.maximize_window()
# Driver.execute_script("window.scrollBy(0,3000)","")
# value=Driver.execute_script("return window.pageYoffset;")
# print("Numder of pixels moved:", value)


# scroll down the page till get element is visible
# flag=Driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img")
# Driver.execute_script("arguments[0].scrollIntoView();", flag)
# value=Driver.execute_script("return window.pageYOffset;")
# print("Number of pixel move:", value)

# i want to scroll down page till end
Driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=Driver.execute_script("return window.pageYOffset;")
print("No of pixel move:" , value )

time.sleep(5)

# i want to scroll up to starting position
Driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value2=Driver.execute_script("return window.pageYOffset;")
print("No of pixel move:" , value )
