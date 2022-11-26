from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import pandas as pd



# Launch browser
serv_object = Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=serv_object)
driver.get("https://customer.i-on.in:9443/signUp")

# read xlsx by pandas
df = pd.read_excel('Input_data.xlsx')


for idx, row in df.iterrows():

    time.sleep(2)
    driver.implicitly_wait(15)

    # Name
    name_field = driver.find_element(By.XPATH, '// *[ @ id = "name"]')
    name_field.clear()
    name_field.send_keys(row['Name'])

    # Select Segment
    select_field = Select(driver.find_element(By.XPATH, '//*[@id="SelectSegment"]'))
    all_options = select_field.options

    for i in all_options:
        if i.text == row['Select Segment']:
            i.click()
            break

    service_required = Select(driver.find_element(By.XPATH, '//*[@id="serviceTypeId"]'))
    all_options2 = service_required.options

    for i in all_options2:
        if i.text == row['Service Required']:
            i.click()
            break

    # pincode
    pincode = driver.find_element(By.XPATH, '//*[@id="Communicationpincode"]')
    pincode.clear()
    pincode.send_keys(row['Pincode'])

    # area
    area = driver.find_element(By.XPATH, '//*[@id="Communicationarea"]')
    area.clear()
    area.send_keys(row['Area/SubArea'])

    # House_no
    house_no = driver.find_element(By.XPATH, '//*[@id="Communicationbuilding"]')
    house_no.clear()
    house_no.send_keys(row['House No.'])

    # City
    city = driver.find_element(By.XPATH, '//*[@id="Communicationcity"]')
    city.clear()
    city.send_keys(row['City'])

    # States
    state = driver.find_element(By.XPATH, '//*[@id="Communicationstate"]')
    state.clear()
    state.send_keys(row['State'])

    # Address 2

    # Pincode
    pincode2 = driver.find_element(By.XPATH, '//*[@id="Installationpin"]')
    pincode2.clear()
    pincode2.send_keys(row['Pincode'])

    # Area
    area2 = driver.find_element(By.XPATH, '//*[@id="Installationarea"]')
    area2.clear()
    area2.send_keys(row['Area/SubArea'])

    # House No.
    house_no2 = driver.find_element(By.XPATH, '//*[@id="Installationbuilding"]')
    house_no2.clear()
    house_no2.send_keys(row['House No.'])

    # City
    city2 = driver.find_element(By.XPATH, '//*[@id="Installationcity"]')
    city2.clear()
    city2.send_keys(row['City'])

    # Status
    state2 = driver.find_element(By.XPATH, '//*[@id="Installationstate"]')
    state2.clear()
    state2.send_keys(row['State'])

    # Email
    email = driver.find_element(By.XPATH, '//*[@id="primaryemail"]')
    email.clear()
    email.send_keys(row['Email '])

    # Mobile
    mobile = driver.find_element(By.XPATH, '//*[@id="mobile"]')
    mobile.clear()
    mobile.send_keys(row['Phone'])

    # Organisation Details
    org_details = driver.find_element(By.XPATH, '//*[@id="Orgnaization"]')
    org_details.clear()
    org_details.send_keys(row['Organization Detail'])

    # Alternative mobile No.
    alt_mobile = driver.find_element(By.XPATH, '//*[@id="alternatemobile"]')
    alt_mobile.clear()
    alt_mobile.send_keys(row['Alternate Phone'])

    # Landline
    landline = driver.find_element(By.XPATH, "//input[@placeholder='LandLine']")
    landline.clear()
    landline.send_keys(row['LandLine'])

    # Society Name
    association_socity = driver.find_element(By.XPATH, "//input[@placeholder='Association/Society Name']")
    association_socity.clear()
    association_socity.send_keys(row['Socity Name'])

    # Society Contact No.
    contact_society = driver.find_element(By.XPATH, '//input[@placeholder="Contact Number Association/Society"]')
    contact_society.clear()
    contact_society.send_keys(row['Society Contact No. '])

    # Society Email
    email_society = driver.find_element(By.XPATH, '//input[@name="AssociationEmail"]')
    email_society.clear()
    email_society.send_keys(row['Society Email'])

print("All rows read successfully...")
print("All data in excel file  data fill up the data entry on screen site ")



