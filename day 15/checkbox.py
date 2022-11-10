from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get("http://the-internet.herokuapp.com/checkboxes")

#Driver.find_element(By.XPATH,"//*[@id='checkboxes']").click()

#lenght of check boxes
check_boxs=Driver.find_elements(By.XPATH,"//form[@id='checkboxes']//input[1]")
print(len(check_boxs))


#click all the check boxes
# for i in range(len(check_boxs)):
#     check_boxs[i].click()


# select the multiple check boxes by choice
for check_box in check_boxs:
    check_boxs=check_box.get_attribute("id")
    if check_box=="checkbox2" or check_box=="check_box1":
          check_box.click()


#select last one checkbox
# if their are 7 check boxes i want to i want to check last  two ckeck boxes ?
# range(5,7)---> (6,7)
#*7-2=5
# totalno_ofelement-2=starting index
# for i in range(len(check_boxs)-2,len(check_boxs)):
#     check_boxs[i].click()


# i want to select first two ceckboxes
for i in range(len(check_boxs)):
    if i>2:
        check_boxs[i].click()









