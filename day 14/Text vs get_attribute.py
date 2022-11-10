#Text  vs get_attribute
# text is always return inner text of the element
# example= <input id="123"  email="xyz"> Email: </input>  = in this html code email is inner text
# get_attribute is return value of any attribute
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("https://admin-demo.nopcommerce.com/login")

element=Driver.find_element(By.ID,"Email")

element.clear()
element.send_keys("adm@yourstore.com")
print("the text value is:",element.text) # print nothig if their is not any inner text of web element
print("the get_attribute value is:",element.get_attribute("value"))