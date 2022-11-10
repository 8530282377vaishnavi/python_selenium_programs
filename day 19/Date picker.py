from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://jqueryui.com/datepicker/")
Driver.maximize_window()

Driver.switch_to.frame(0)

# Driver.find_element(By.XPATH,"//*[@id='datepicker']").send_keys("11/2/2022")

year="2022"
month="April"
Date="30"
Driver.find_element(By.XPATH,"//*[@id='datepicker']").click()

# while True:
#
#     Mon=Driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
#     yr=Driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
#
#     if Mon==month and yr==year:
#       break;
#     else:
#         #Driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()
#         Driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
#
#
# dates=Driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# Mon = Driver.find_elements(By.XPATH, "//span[@class='ui-datepicker-month']")
# yr=Driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text


# for i in dates:
#     if i.text==Date:
#         i.click()
#         break

https://bookonwardticket.com/
Driver.find_element(By.XPATH,"//*[@id='onward-departure-date']")
Dropcountry=Select(Driver.find_element(By.XPATH,"//select[@id='input-country']"))

Datepicker_month=select(Driver.find_elements(By.XPATH,"//select[@class='ui-datepicker-month']"))
Datepicker_month.select_