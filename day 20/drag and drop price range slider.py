from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_object=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_object)

Driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
Driver.maximize_window()

min_slider=Driver.find_element(By.XPATH,"//*[@id='slider-range']/span[1]")
max_slider=Driver.find_element(By.XPATH,"//*[@id='slider-range']/span[2]")

print("currunt location of slider before moving is.....")
print(min_slider.location)  #{'x': 59, 'y': 250}
print(max_slider.location) #{'x': 545, 'y': 250}

act=ActionChains(Driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(max_slider,-40,0).perform()

print("Lication of the slider after moving .......")
print(min_slider.location) #{'x': 161, 'y': 250}
print(max_slider.location) #{'x': 506, 'y': 250}
