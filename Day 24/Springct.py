# 1. Navigate to - https://demoblaze.com/index.html
# Login using following credentials::
# 	sctqaautomation@grr.la
# 	Spring@123

# 2. Under the PHONES section there are few devices listed with their specification.
# 3. Select Samsung Galaxy S6 and add it to the cart
# 4. Click on Home menu on the top and click on LAPTOP option
# 5. Add Dell i7 8 GB to the cart
# 6. Click on Home menu and the top and click on MONITOR option
# 5. Add Asus Full HD monitor to the cart
# 6. Navigate to the cart menu
#  7. Cart will comprise of 3 products, sort them as per the cost from Lowest to Highest and print them on console
# 8. Fetch price of the items and sum it such that total value should be equal to summed up value
# 9. Click on Place Order and enter information
# 10. Complete purchase and extract ID and Amount
# 11. Print those values on console


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)
Driver.get("https://demoblaze.com/index.html")
login=Driver.find_element(By.ID,"login2")
login.click()
alert=Driver.switch_to.alert
# alertwindow=Driver.switch_to.alert
# alertwindow=Driver.switch_to.alert
# print(alertwindow.text)
alert.find_element(By.XPATH,"//input[@type='text']").send_keys("sctqaautomation@grr.la")

# # enter the email
# Driver.find_element(By.XPATH,"//input[@type='text']").send_keys("sctqaautomation@grr.la")
#
# # enter the password
# Driver.find_element(By.XPATH,"//input[@type='password']").send_keys("Spring@123")
#
# # click the login button
# Driver.find_element(By.XPATH,'//button[@onclick="logIn()"]').click()
#
# # change control to main page
# Driver.switch_to.window(main)
#
#
#
# # closing the window
# Driver.quit()
Driver.find_element(By.LINK_TEXT,"Phones").click()
Driver.find_element(By.LINK_TEXT,"Samsung galaxy s6").click()
Driver.find_element(By.XPATH,'//a[@onclick="addToCart(1)"]').click()
alertwindow=Driver.switch_to.alert
alertwindow.accept()
Driver.find_element(By.LINK_TEXT,"Laptops").click()
Driver.find_element(By.LINK_TEXT,"Dell i7 8gb").click()
Driver.find_element(By.XPATH,"//a[@onclick='addToCart(12)']").click()
alertwindow=Driver.switch_to.alert
alertwindow.accept()
Driver.find_element(By.XPATH,"//a[@id='itemc']").click()
Driver.find_element(By.LINK_TEXT,"ASUS Full HD").click()
Driver.find_element(By.XPATH,'//a[@onclick="addToCart(14)"]').click()
alertwindow=Driver.switch_to.alert
alertwindow.accept()

Driver.find_element(By.XPATH,'//a[@onclick="showcart()"]').click()

num1=Driver.find_element(By.XPATH,"document.querySelector(tbody tr:nth-child(1)td:nth-child(1)")
num2=Driver.find_element(By.XPATH,'$("tbody tr:nth-child(1) td:nth-child(1)")')
num3=Driver.find_element(By.XPATH,'$("tbody tr:nth-child(1) td:nth-child(1)")')

list=[num1,num2,num3]
list.sort()
print(list)

Driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()

Driver.switch_to.window()
Driver.find_element(By.XPATH,"//input[@id='name']").send_keys("xyz")
Driver.find_element(By.XPATH,"//input[@id='country']").send_keys("india")
Driver.find_element(By.XPATH,"//input[@id='city']").send_keys("pune")
Driver.find_element(By.XPATH,"//input[@id='card']").send_keys("abcd")
Driver.find_element(By.XPATH,"//input[@id='month']").send_keys("jully")
Driver.find_element(By.XPATH,"//input[@id='year']").send_keys(2022)
Driver.find_element(By.XPATH,"//button[@onclick='purchaseOrder()']").click





