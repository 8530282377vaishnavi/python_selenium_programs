from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

source = "C SHIVAJI MAH T - CSTM"
destination = "HOWRAH JN - HWH"
def launch_browser():
    global driver
    option = Options()
    option.add_argument("--disable-infobars")
    option.add_argument("start-maximized")
    option.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    option.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    # Launch the browser
    serv_object = Service("C:\web drivers selenium\chromedriver_win32 (1)\chromedriver.exe")
    driver = webdriver.Chrome(service=serv_object, options=option)
    driver.get("https://www.irctc.co.in/nget/train-search")





def search_train():
    #  1. Fill From - "C SHIVAJI MAH T - CSTM"
    #                 To - "HOWRAH JN - HWH"
    from_field = driver.find_element(By.XPATH, "//input[@aria-autocomplete='list']")
    from_field.send_keys(source)
    from_field.send_keys(Keys.TAB)

    to_field = driver.find_element(By.XPATH, "//*[@id='destination']/span/input")
    to_field.send_keys(destination)
    to_field.send_keys(Keys.TAB)

    # Select date
    act = ActionChains(driver)
    date_field = driver.find_element(By.XPATH, "//span[@class='ng-tns-c58-10 ui-calendar']")
    date_field.click()
    driver.find_element(By.XPATH, "//span[@class='ui-datepicker-next-icon pi pi-chevron-right ng-tns-c58-10']").click()
    next = driver.find_element(By.XPATH,
                               "//div[@class='ui-datepicker-calendar-container ng-tns-c58-10 ng-star-inserted']")
    date = driver.find_element(By.XPATH,
                               "//*[@class='ui-datepicker-calendar ng-tns-c58-10']/tbody/tr/td//a[text()='26']")
    act.move_to_element(next).move_to_element(date).click().perform()

    # # As "TATKAL" option is not present so select "LADIES" quota
    dropdown_ops = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]')
    dropdown_ops.click()
    dropdown_ops2 = driver.find_element(By.XPATH, '//*[@id="journeyQuota"]/div/div[4]/div/ul/p-dropdownitem[2]/li')
    dropdown_ops2.click()

    #   Select "AC 3 Tier (3A)"
    drop_class = driver.find_element(By.XPATH, "//*[@id='journeyClass']")
    drop_class.click()
    drop_class2 = driver.find_element(By.XPATH, '//*[@id="journeyClass"]/div/div[4]/div/ul/p-dropdownitem[8]/li/span')
    drop_class2.click()

    #  Select "Train with Available Berth"
    check_box = driver.find_element(By.XPATH, "//*[text()='Train with Available Berth ']")
    check_box.click()

    #  Click on Search
    search = driver.find_element(By.XPATH, "//*[text()='Search']")
    search.click()

launch_browser()
search_train()


















