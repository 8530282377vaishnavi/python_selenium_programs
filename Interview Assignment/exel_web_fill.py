from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


# Imports
import csv
import requests
from selenium import webdriver
import time

#-------------------------------------------------------------------------------



serv_object = Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=serv_object)
driver.get("https://customer.i-on.in:9443/signUp")

with open('Data.csv', 'r') as csv_file:

    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    print("File started processing...")
# Web Automation

    for line in csv_reader:

        time.sleep(2)
        driver.implicitly_wait(15)
        name_field = driver.find_element(By.XPATH,'// *[ @ id = "name"]')
        name_field.clear()
        name_field.send_keys(line[0])

        select_field= Select(driver.find_element(By.XPATH,'//*[@id="SelectSegment"]'))
        alloptions = select_field.options

        for i in alloptions:
            if i.text ==line[1]:
                i.click()
                break


        service_required=Select(driver.find_element(By.XPATH,'//*[@id="serviceTypeId"]'))
        alloptions2 = service_required.options

        for i in alloptions2:
            if i.text == line[2]:
                i.click()
                break


        # pincode
        pincode=driver.find_element(By.XPATH,'//*[@id="Communicationpincode"]')
        pincode.clear()
        pincode.send_keys(line[3])

        # area
        area = driver.find_element(By.XPATH, '//*[@id="Communicationarea"]')
        area.clear()
        area.send_keys(line[4])

        house_no = driver.find_element(By.XPATH, '//*[@id="Communicationbuilding"]')
        house_no.clear()
        house_no.send_keys(line[5])

        city = driver.find_element(By.XPATH, '//*[@id="Communicationcity"]')
        city.clear()
        city.send_keys(line[6])

        state = driver.find_element(By.XPATH, '//*[@id="Communicationstate"]')
        state.clear()
        state.send_keys(line[7])

        # address 2
        # pincode
        pincode2 = driver.find_element(By.XPATH, '//*[@id="Installationpin"]')
        pincode2.clear()
        pincode2.send_keys(line[8])

        # area
        area2 = driver.find_element(By.XPATH, '//*[@id="Installationarea"]')
        area2.clear()
        area2.send_keys(line[9])

        house_no2 = driver.find_element(By.XPATH, '//*[@id="Installationbuilding"]')
        house_no2.clear()
        house_no2.send_keys(line[10])

        city2 = driver.find_element(By.XPATH, '//*[@id="Installationcity"]')
        city2.clear()
        city2.send_keys(line[11])

        state2 = driver.find_element(By.XPATH, '//*[@id="Installationstate"]')
        state2.clear()
        state2.send_keys(line[12])

        email = driver.find_element(By.XPATH, '//*[@id="primaryemail"]')
        email.clear()
        email.send_keys(line[14])

        mobile = driver.find_element(By.XPATH,'//*[@id="mobile"]')
        mobile.clear()
        mobile.send_keys(line[15])

        org_details = driver.find_element(By.XPATH, '//*[@id="Orgnaization"]')
        org_details.clear()
        org_details.send_keys(line[16])

        alt_mobile = driver.find_element(By.XPATH, '//*[@id="alternatemobile"]')
        alt_mobile.clear()
        alt_mobile.send_keys(line[17])

        landline = driver.find_element(By.XPATH, "//input[@placeholder='LandLine']")
        landline.clear()
        landline.send_keys(line[18])

        association_socity = driver.find_element(By.XPATH, "//input[@placeholder='Association/Society Name']")
        association_socity.clear()
        association_socity.send_keys(line[19])

        contact_socity = driver.find_element(By.XPATH, '//input[@placeholder="Contact Number Association/Society"]')
        contact_socity.clear()
        contact_socity.send_keys(line[20])

        email_socity = driver.find_element(By.XPATH, '//input[@name="AssociationEmail"]')
        email_socity.clear()
        email_socity.send_keys(line[21])


    print("All rows read successfully...")
















        # age_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        # age_field.send_keys(line[1])
        #
        # score_field = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        # score_field.send_keys(line[2])
        #
        # submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span')
        # submit.click()