# links == 1. internal link --> when i click the link this get nevigate into same link page
#2. External link-->when click on this link this link goes to anothe pagek
#3. broken link-->when click on this link not any page display


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("https://demo.nopcommerce.com/")
Driver.maximize_window()
Driver.minimize_window()
#Driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()
#Driver.find_element(By.LINK_TEXT,"Digital downloads").click()

# i want to find how many links are available on the page 
Links=Driver.find_elements(By.TAG_NAME,"a")
#Links=Driver.find_elements(By.XPATH,"//a")
print("The total no. of links available in page:",len(Links))

#i want know the names of the links
for Link in Links:
    print(Link.text)



# how to handle broken link
#Broken link==Dosent have any target page
# main point all the broken link which is error code greater than 400 and normal link which is less than 400
# less than 400 error is responce code and greater than 400 is error code



