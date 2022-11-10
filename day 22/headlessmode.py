#Headless mode Testiong : it is nothing but their are execution of test cases with oute UI
# Backend
# Advantage is we can do multiple task parley and  execution will be very faster

from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    Driver = webdriver.Chrome(service=serv_obj,options=ops)
    return Driver

Driver=headless_chrome()
Driver.get("https://demo.nopcommerce.com/'")
print(Driver.title)
print(Driver.current_url)
Driver.close()

