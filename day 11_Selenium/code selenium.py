
from selenium import webdriver
from selenium.webdriver.common.service import Service
serv_obj = Service( "C:\web drivers selenium\chromedriver_win32\chromedriver.exe" )
Driver = webdriver.Chrome(service=serv_obj)
Driver.get("https://admin-demo.nopcommerce.com/login")

