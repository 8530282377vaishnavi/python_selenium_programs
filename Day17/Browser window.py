from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://www.instagram.com/accounts/login/")
Driver.maximize_window()

Links=Driver.find_elements(By.TAG_NAME,"a")
#Links=Driver.find_elements(By.XPATH,"//a")
print("The total no. of links available in page:",len(Links))


# for link in Links:
#     print(link.text)
#
# for i in range(len(Links)):
#   if Links[i] == "Instagram Lite":
#     print(i)

# Windowid=Driver.current_window_handle
# print(Windowid)   #CDwindow-EBE49848E985358D7DA0FFBE9D9AD42E
#                   #CDwindow-4993F48DFA5DEDC1B39D73D23A4324D6  (the browser windo id is dynimic all the time when i open same page in differrent window this id is always unique  )

Driver.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div/div[3]/div/a[1]/img").click()
Driver.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/div/div[3]/div/a[2]/img").click()

WindowIDs=Driver.window_handles


parentwindowid=WindowIDs[0]
childwindowid=WindowIDs[1]
childwindowid2=WindowIDs[2]
print(parentwindowid, childwindowid, childwindowid2)

Driver.switch_to.window(childwindowid)
print(Driver.title)

Driver.switch_to.window(parentwindowid)
print(Driver.title)
#
#approch 2

# for win  in WindowIDs:
#     Driver.switch_to.window(win)
#     print(Driver.title)
#
#
# # for close  the single window
# for win in WindowIDs:
#     Driver.switch_to.window(win)
#     if Driver.title=="Login • Instagram":
#         Driver.close()


#for close the multiple window  based up on our choice  .close specific browser
for win in WindowIDs:
    Driver.switch_to.window(win)
    if Driver.title=="Login • Instagram" or Driver.title=="XYZ":
        Driver.close()



