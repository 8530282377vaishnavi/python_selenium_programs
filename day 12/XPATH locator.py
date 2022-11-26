# XPATH is called as xml path
# XPATH is an syntax or language to find the element using the xml path expression
# it is find the  loction of element on web page using the HTML DMO structure
# the XPATH can be navigate through the attribute and element in DMO structure
# XPAtH is an address of the element
# their are two types of XPATH ---> 1) Absolute XPATH/ Full XPATH ,  2) Relative XPATH/Partial XAPTH
# 1) absolute XPATH/Full XPATH=  1)The full XPATH is nevigate from root node
                            #    2)Start with single  shash/
                            #    3) Only use in HTML we call them as  tag/ in XML we call them as nodes
                            # example : /html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input
                            # /html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input
# 2) Relative XPATH/Partial XPATH = 1)The partial XPATH is directly jump to respective element on DMO
                            #       2) Start with double slash  //
                            #       3) its use attributes with value
                            ## example : //*[@id="email"]
                            # //input[name="email"]
# selector hub is their to write a path
# how to capture xpath
# for capturing xpath last 3 year back the fire fox provided the fire bug and fire path but for some security issue it was depricated
# but currunt days all browsers provided the = right click on element--> inspect-->highlighting html code---> right click--> copy path
#  selector hub = download selector hub --> Chrome,edge,firefox differnt selectorhub is present download it---> below the html code ---> nevigation is there click it --> then find the loctors,xpath easily
# which XPATH is mostly use ? and why?
#--> the relative xpath is mostly use becoz. 1) if the developer is develop new element that time absolute path is broken .
                                          #  2) if developer change the location of element that time also absolute path is broken
                                          #  3) The absolute path is always unstable
# with the XPATH we can use differnt method such as--> and, or, contains(), start-with(),text()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("C:\web drivers selenium\chromedriver_win32/chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)
Driver.get("http://automationpractice.com/index.php")
Driver.maximize_window()
# Absolute XPATH
# Driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/input[4]").send_keys("T-shirts")
# Driver.find_element(By.XPATH,"/html/body/div/div[1]/header/div[3]/div/div/div[2]/form/button").submit()

# relative XPATH
# Driver.find_element(By.XPATH,"//input[@id='search_query_top']").send_keys("T-shirt")
# Driver.find_element(By.XPATH,"//button[@name='submit_search']").submit()

#with the XPATH we can use differnt method such as--> and, or, contains(), start-with(),text()

# or operator & and operator
# Driver.find_element(By.XPATH,"//input[@id='search_query_top' or @name='search_query']").send_keys("tops")
# Driver.find_element(By.XPATH,"//button[@name='submit_search' and @type='submit']").click()

# contains and start-with
# Driver.find_element(By.XPATH,"//input[contains(@id,'search')]").send_keys("T-shirt")
# Driver.find_element(By.XPATH,"//input[starts-with(@name,'s')]").submit()

# text = identify the element using inner text
#Driver.find_element(By.XPATH,"//a[text()='T-shirts']").click()
#Driver.find_element(By.XPATH,"//a[text()='T-shirts']").click()






