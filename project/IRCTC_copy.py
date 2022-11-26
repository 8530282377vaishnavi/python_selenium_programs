from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
serv_object = Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=serv_object, options=option)
driver.get("https://www.irctc.co.in/nget/train-search")

# driver.find_element(By.XPATH,'//*[@id="login_header_disable"]/div/div/div[2]/a').click()

from_field=driver.find_element(By.XPATH,"//input[@aria-autocomplete='list']")
from_field.send_keys("C SHIVAJI MAH T - CSTM")
from_field.send_keys(Keys.TAB)

to_field= driver.find_element(By.XPATH,"//*[@id='destination']/span/input")
to_field.send_keys("HOWRAH JN - HWH")
to_field.send_keys(Keys.TAB)


date_field=driver.find_element(By.XPATH,"//span[@class='ng-tns-c58-10 ui-calendar']").click()
print("Hii")
driver.find_element(By.XPATH,"//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c58-10']").click()
print("Hii")
act=ActionChains(driver)
next=driver.find_element(By.XPATH,"//div[@class='ui-datepicker-calendar-container ng-tns-c58-10 ng-star-inserted']")
print("hi")
date=driver.find_element(By.XPATH,"//*[@class='ui-datepicker-calendar ng-tns-c58-10']/tbody/tr/td//a[text()='23']")

act.move_to_element(next).move_to_element(date).click().perform()

dropdown_ops=driver.find_element(By.XPATH,'//*[@id="journeyQuota"]')
dropdown_ops.click()
dropdown_ops2=driver.find_element(By.XPATH,'//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[2]/li')
dropdown_ops2.click()

# all class
drop_class=driver.find_element(By.XPATH,"//*[@id='journeyClass']")
drop_class.click()
drop_class2=driver.find_element(By.XPATH,'//*[@id="journeyClass"]/div/div[4]/div/ul/p-dropdownitem[8]/li/span')
drop_class2.click()

check_box=driver.find_element(By.XPATH,"//*[text()='Train with Available Berth ']")
check_box.click()

search=driver.find_element(By.XPATH,"//*[text()='Search']")
search.click()
# drop_class=driver.find_element(By.XPATH,"//*[@id='journeyClass']/div/div[3]")
# drop_class2=driver.find_element(By.XPATH,"//*[@aria-label='AC 3 Tier (3A)']")










# driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar ng-tns-c58-10']/tbody/tr[4]/td[6]/a/text()")
# # //*[@id="jDate"]/span/div/div/div[2]/table/tbody/tr[4]/td[6]/a/text()
# date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar ng-tns-c58-10']/tbody/tr[4]")
# print(len(date))
# for i in date:
#     if i=="23":
#       i.click()
#       break


# "//div[@class='ui-datepicker-calendar-container ng-tns-c58-10 ng-star-inserted']"



# driver.find_element(By.XPATH,"//table/tbody/tr/td//a[@class='ui-state-default ng-tns-c58-10 ng-star-inserted'][text()='13']").click()
# print(len(date1))
# print(date1)

# print("Hii")
# m=driver.find_elements(By.XPATH,"//table/tbody/tr/td")
# print("length",len(m))
# for i in m:
#     d=i.get_attribute("value")
#     print("length2",d)
#     if d==23:
#          i.click()
# date_1="23"
# for dates in m:
   # if (dates.is_enabled() and  dates.is_displayed() =="23"):
   #       dates.click()
   # if dates.text=="23":
       # dates.click()
#         break
print("ok")








#


# driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar ng-tns-c58-10']/tbody/tr[4]/td[6]/a/text()")
# # //*[@id="jDate"]/span/div/div/div[2]/table/tbody/tr[4]/td[6]/a/text()
# date=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar ng-tns-c58-10']/tbody/tr[4]")
# print(len(date))
# for i in date:
#     if i=="23":
#       i.click()
#       break


# "//div[@class='ui-datepicker-calendar-container ng-tns-c58-10 ng-star-inserted']"



# driver.find_element(By.XPATH,"//table/tbody/tr/td//a[@class='ui-state-default ng-tns-c58-10 ng-star-inserted'][text()='13']").click()
# print(len(date1))
# print(date1)

# print("Hii")
# m=driver.find_elements(By.XPATH,"//table/tbody/tr/td")
# print("length",len(m))
# for i in m:
#     d=i.get_attribute("value")
#     print("length2",d)
#     if d==23:
#          i.click()
# date_1="23"
# for dates in m:
   # if (dates.is_enabled() and  dates.is_displayed() =="23"):
   #       dates.click()
   # if dates.text=="23":
       # dates.click()
#         break
print("ok")

