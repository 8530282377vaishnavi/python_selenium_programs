# Dropdown
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("https://www.opencart.com/index.php?route=account/register")
Driver.maximize_window()

Dropcountry=Select(Driver.find_element(By.XPATH,"//select[@id='input-country']"))

# Dropcountry.select_by_visible_text("Algeria") #  bultin function
#Dropcountry.select_by_value("3")
Dropcountry.select_by_index("4")

# findout total no. of options
alloptions=Dropcountry.options
print(len(alloptions))

# to print all the text
for options in alloptions:
    print(options.text)

#select option from dropdown without using bult in function
for option in alloptions:
    if option.text=="India":
        option.click()
        break

# i want to capture all the option from dropdown
# allelement=Driver.find_elements(By.XPATH,"//select[@id='input-country']//option")
# print(len(allelement))