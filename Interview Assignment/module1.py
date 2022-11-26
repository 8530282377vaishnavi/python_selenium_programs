from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

try:

     serv_object = Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
     driver = webdriver.Chrome(service=serv_object)

     driver.get(r'https://accounts.google.com/ServiceLogin/identifier?elo=1&ifkv=ARgdvAsaClzsa7EAkjbA7559tXue_BaNVOUo562_RXCHYSGhPwdPOAXkmsLxrZfc1kjao7TPe3-J&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
     driver.maximize_window()
     driver.implicitly_wait(15)

     login_Box = driver.find_element(By.XPATH, '//*[@id ="identifierId"]')
     login_Box.send_keys("patilvaishu905@gmail.com")

     next_Button = driver.find_elements(By.XPATH, '//*[@id ="identifierNext"]')
     next_Button[0].click()

     passWord_Box = driver.find_element(By.XPATH,
          '//*[@id ="password"]/div[1]/div / div[1]/input')
     passWord_Box.send_keys("vaishnavi@ajinkya29")

     next_Button_2= driver.find_elements(By.XPATH, '//*[@id ="passwordNext"]')
     next_Button_2[0].click()
     driver.switch_to.default_content()

     print('Login Successful...!!')
except:
     print('Login Failed')



google_app_menu1 = driver.find_element(By.XPATH, "//a[@aria-label='Google apps']")
google_app_menu1.click()
google_app_menu2 = driver.find_element(By.XPATH, "//a[@aria-label='Google apps']")
google_app_menu2.click()
driver.switch_to.frame(driver.find_element(By.TAG_NAME,'iframe'))


driver.get('https://mail.google.com/mail/u/0/#inbox?compose=new')

to_field = driver.find_element(By.XPATH,"//input[@role='combobox' and @type='text' and @aria-owns=':cz']")
to_field.send_keys("patilvaishu905@gmail.com")

subject_field = driver.find_element(By.XPATH,"//input[@name='subjectbox' and @placeholder='Subject']")
subject_field.send_keys("Automation Testing Profile")

mail_body=driver.find_element(By.XPATH,"//div[@class='Am Al editable LW-avf tS-tW']")
mail_body.click()

attachments=driver.find_element(By.XPATH,"//div[@class='a1 aaA aMZ']")
attachments.click()


Upload_file = driver.find_element(By.XPATH,'//input[@type="file"]').send_keys(r"C:\Users\Sujay Sankpal\OneDrive\Desktop\T.pdf")
send=driver.find_element(By.XPATH,"//div[@class='T-I J-J5-Ji aoO v7 T-I-atl L3'][text()='Send']").click()

print("Email Send Successfully")


