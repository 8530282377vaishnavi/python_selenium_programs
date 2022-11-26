# All explanation  in notebook (software testing notebook )
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service(" C :\ web drivers selenium\ chromedriver_win32 (1)\chromedriver.exe ")
Driver=webdriver.Chrome(service=serv_obj)

# self node axes in XPATH
# text= capture the txt value of element store into the variable and print it
Driver.get("https://money.rediff.com/gainers")
# text_msg=Driver.find_element(By.XPATH,"//a[contains(text(),'Anjani Finance Ltd.')]/self::a").text
# print(text_msg)
#
# text_msg2=Driver.find_element(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/self::a").text
# print(text_msg2)

#parent
# text_msg2=Driver.find_element(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/parent::td").text
# print(text_msg2)

# child
# child=Driver.find_elements(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/ancestor::tr/child::td")
# print(len(child)) # ans=5
# #print(len(child))

# ancestor
# child=Driver.find_element(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/ancestor::tr").text
# print(child)

#descendant node
child2=Driver.find_elements(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/ancestor::tr/descendant::*")
print("No.of descendant nodes are:",len(child2))
#
# following
following=Driver.find_elements(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/ancestor::tr/following::*")
print("No.of following nodes are:",len(following))

#following-sibling
following_sibling=Driver.find_elements(By.XPATH,"//a[contains(text(),'Indl.&Prud.Invst')]/ancestor::tr/following-sibling::*")
print("No.of following-sibling nodes are:",len(following_sibling))

#preceding
preceding=Driver.find_elements(By.XPATH,"//a[contains(text(),'Emmessar Biotech')]/ancestor::tr/preceding::*")
print("No.of following-sibling nodes are:",len(preceding))

#preceding sibling
preceding_sibling=Driver.find_elements(By.XPATH,"//a[contains(text(),'Emmessar Biotech')]/ancestor::tr/preceding-sibling::*")
print("No.preceding_sibling nodes are:",len(preceding_sibling))