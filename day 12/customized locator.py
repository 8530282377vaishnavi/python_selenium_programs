# CSS Selectors and XPATH are customized locator= why becoz we can not find directly in Html
# CSS- Cascading Style Sheet- different combinations we use like Tag and ID, Tag and class, Tag and attribute, tag and class, attribute
# Tag and ID combination
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
ser_obj= Service("C:\web drivers selenium\chromedriver_win32/chromedriver.exe")
Driver = webdriver.Chrome(service=ser_obj)

Driver.get("https://www.facebook.com/")
# for tag and id we use hash tag  (tag#id)
# with tagname
#Driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("patilvv.123vgs@gmail.com")
# without tagname
#Driver.find_element(By.CSS_SELECTOR,"#email").send_keys("patilvv.123vgs@gmail.com ")

# Tag and class= for class e use dot(tag.class)
#Driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("Vishwas")
#Driver.find_element(By.CSS_SELECTOR,"._6luy ").send_keys("Vishwas")

# tag and attribute we write tagname[attribute=value]
#with tagname
#Driver.find_element(By.CSS_SELECTOR,"input[placeholder=Password]").send_keys("avs")
#without tagname
#Driver.find_element(By.CSS_SELECTOR,"[placeholder=Password]").send_keys("avs")


# Tag,class and attribute then use tagname.valueofclass[attribute=value]
# with tagname
#Driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=email]").send_keys("aa")
# without tagname

Driver.find_element(By.CSS_SELECTOR,".inputtext[name=email]").send_keys("bb")


