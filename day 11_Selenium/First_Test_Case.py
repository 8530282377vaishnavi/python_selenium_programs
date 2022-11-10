'''1)Open Web Browser (Chrome/ Firefox/ IE)
2)Open URL https://admin-demo.nopcommerce.com/login
3)Provide Email- admin@yourstore.com
4)Provide Password-admin
5) Click on the login
6) Capture the title of the dashboard page. (Actual Title)
7)Verify the Title of the page: “Dashboard / nopCommerce Administration” (Expected)
8) Close Browser '''

# selinium 3
#from selenium import webdriver
# Driver=webdriver.Chrome(executable_path="C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
# Driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# Driver.find_element("username").send_keys("Admin")
# Driver.find_element("password").send_keys("admin123")
# Driver.find_element("oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()
# #oxd-button oxd-button--medium oxd-button--main orangehrm-login-button
# act_title=Driver.title
# exp_title="OrangeHRM"
# if act_title==exp_title:
#     print("Login Test Pass")
# else:
#     print("Login Test Is Fail")
# Driver.close()

# selenium 4
from selenium import webdriver
from selenium.webdriver.chrome.service  import Service
#from selenium.webdriver.common.by import By
serv_obj= Service( " C:\web drivers selenium\chromedriver_win32\chromedriver.exe " )
try:
 Driver= webdriver.Chrome(service=serv_obj)

finally:print("error is occure")

Driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

'''Driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("Admin")
Driver.find_element(By.XPATH, "//input[@class='oxd-input oxd-input--active']").send_keys("admin123")
Driver.find_element(By.XPATH, "//button[@class='oxd-button oxd-button--medium oxd-button--main orangehrm-login-button']" ).click()'''
#oxd-button oxd-button--medium oxd-button--main orangehrm-login-button
#
act_title=Driver.title
exp_title="OrangeHRM"
if act_title==exp_title:
    print("Login Test Pass")
else:
    print("Login Test Is Fail")
Driver.close()

