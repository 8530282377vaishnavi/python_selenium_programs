# web table their are two types
# 1) static table = table size,order,rows,columns are fixed
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_object=Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://testautomationpractice.blogspot.com/")
Driver.maximize_window()

# how to count no. of rows and columns
No_of_rows=len(Driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))

No_of_columons=len(Driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
print(No_of_rows)
print(No_of_columons)



#How to read specific rows and columon from the table
Data=Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[4]/td[1]").text
print(Data)

# i want to read all the data from the table
for r in range(2,No_of_rows+1):
    for c in range(1,No_of_columons+1):
        Data = Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td["+str(c)+"]").text  # for dynamic web table
        print(Data,end="                       ")
    print()


#
# for r in range(2,No_of_rows+1):
#     authername=Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
#     if authername=="Mukesh":
#         Bookname=Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+    "]/td[1]").text
#
#         print(authername,"     ", Bookname)
# Driver.close()


for r in range(2,No_of_rows+1):
    authername=Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+"]/td[2]").text
    if authername=="Mukesh":
        Bookname=Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+    "]/td[1]").text
        price=Driver.find_element(By.XPATH,"//table[@name='BookTable']//tr["+str(r)+    "]/td[4]").text
        print(authername,"    ", Bookname,"    ",price)
