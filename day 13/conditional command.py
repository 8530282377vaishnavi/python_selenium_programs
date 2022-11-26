# conditional commands is used for behavioural testing = such as to check the redio buttons,check box
# conditional commands such as is_display(), is_selected(), is_enable()
# always give answer in true or false
# only conditional can be access through webelements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object = Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")

Driver = webdriver.Chrome(service=serv_object)

Driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

# is_display and is_enable = method
searchbox = Driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
print("Display status:", searchbox.is_displayed())
print("Enable status:", searchbox.is_enabled())

# is_selected = is for radio buttons and check box
print("defult radio button status..... ")
RD_male= Driver.find_element(By.XPATH," //input[@id='gender-male']")
print(RD_male.is_selected())


RD_female=Driver.find_element(By.XPATH,"//input[@id='gender-female']")
print(RD_female.is_selected())

RD_male.click()


print("After selecting male redio button status....... ")
print(RD_male.is_selected())
print(RD_female.is_selected())


RD_female.click()
print("After selecting female redio button status....... ")
print(RD_male.is_selected())
print(RD_female.is_selected())





Driver.quit()
