# cookies are nothing but temporary files created by the browser whenever you browse some website
# every cookie which contain a multiple attribue and each contain a single value

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get('https://demo.nopcommerce.com/')
cookies=Driver.get_cookies()
print("lenght of cookies:",len(cookies))   # ho many cookies are present count

# print details of all the  cookies #present in dictionary collection format
# for c in cookies:
#     print(c)

#
# for c in cookies:
#     print(c.get("name"), c.get("value"))


# add new  cookie to the browser
Driver.add_cookie({"name":"MyCookie", "value":"1124567"})
Cookies=Driver.get_cookies()
print("lenght of cookies after adding :",len(Cookies))

# delete the cookies
Driver.delete_cookie("MyCookie")
cookies1=Driver.get_cookies()
print("lenght of cookies after deleting :",len(cookies1))

# delete all the cookies
Driver.delete_all_cookies()
cookies2=Driver.get_cookies()
print("lenght of cookies after deleting :",len(cookies2))

