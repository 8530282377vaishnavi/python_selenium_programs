"""from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('C:\web drivers selenium\chromedriver_win32/chromedriver.exe')
driver= webdriver.Chrome(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
#  ALL NAME,ID, TAG NAME,CLASS NAME, LINK TEXT, PARTIAL LINK TEXT ALL ARE LOCATOR
driver.find_element(By.TAG_NAME,"img").click()
driver.find_element(By.NAME,"email").send_keys("patilvv,123vgs@gmail.com")
driver.find_element(By.ID,"pass").send_keys("vaishnavi@1997")
driver.find_element(By.NAME,"login").submit()
driver.find_element(By.CLASS_NAME,"_97w3").click()"""

# try:

#  driver.find_elements(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# except:
#     print("successfully launch the page")
# try:
#  driver.find_element(By.LINK_TEXT,"Register").click()
# except:
#  print("register successfully")
#
# try:
#     driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
# except:
#     print("Partial link_txt use properly")

# to find multiple web element find_elements is use with CLASS_NAME  ,,
# # class name and tag name is used to find one or two element
# # class name and tag name is same most of the time for multiple elements
# driver.find_element (By.CLASS_NAME,"button-1 register-next-step-button").click()
#
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service('C:\web drivers selenium\chromedriver_win32/chromedriver.exe')
driver= webdriver.Chrome(service=serv_obj)
driver.get("http://automationpractice.com/index.php")
driver.maximize_window()

sliders=driver.find_elements(By.CLASS_NAME,"homeslider-container")
print(len(sliders))#5 gives a total no. of images

links=driver.find_elements(By.TAG_NAME,"a")
print(len(links)) #149 links of "a" is present in the side

driver.find_element(By.CLASS_NAME,"login").click()


