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
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv)
Driver.get("https://demoblaze.com/index.html")


