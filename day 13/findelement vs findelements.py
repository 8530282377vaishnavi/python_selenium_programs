# find_element vs find_elements
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("https://demo.nopcommerce.com/login")

############################  find element= Returns single webelement
# Senario first= Locator matching with single webelement
# element=Driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple iCam")

# Senario second = locator matching with multiple webelementd
# element2=Driver.find_element(By.XPATH,"//div[@class='footer-upper']//a")
#print(element2.text)# it will show only firrst link from the footer  "Sitemap"

# Senario third= If element not available then throw no such element  exception
# element3= Driver.find_element(By.CLASS_NAME,"-login")  # traceback error has shown
# element3.click()


########################## Find_elements =1) Return multiple webelement
                        #               2) Find_eleements always return a list collection (it return single webelement in the form of list )
# senario first = Locator matching with single webelement
element4= Driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
print(len(element4))  # such as the no. of elements is 1
# main point find eleements  always return in list collection
element4[0].send_keys("Apple iCam")  # write the index no.


# senario second= Locator matching with multiple webelement webelement
element5=Driver.find_elements(By.XPATH,"//div[@class='footer-upper']//a")
print(len(element5))
print(element5[1].text)  #when i want to print single text

# when i want to display all the text links   using for loop
# for ele in element5:
#     print(ele.text)


#Senario third= If element not available  then by using find_elements
element6= Driver.find_elements(By.CLASS_NAME,"-login")  # not any show becoz the elements are store in list then it returns always zero
print("Element returns=",len(element6))  # result=Element returns= 0




Driver.quit()




