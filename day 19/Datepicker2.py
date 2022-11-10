
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://www.globalsqa.com/demo-site/datepicker/")
Driver.maximize_window()

Driver.find_element(By.XPATH,"//*[@id='DropDown DatePicker']").click()


Driver.find_element(By.XPATH,"//*[@id=onward-departure-date']").click()
Date_month=Select(Driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
Date_month.select_by_visible_text("Dec")

Date_year=Select(Driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
Date_year.select_by_visible_text("2022")

all_dates=Driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td")

for date in all_dates:
    if date.text==25:
        date.click()
        break


