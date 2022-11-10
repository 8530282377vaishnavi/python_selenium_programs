from selenium import webdriver
from day22 import xlutils.py
from selenium.webdriver.chrome.service import Service
serv_obj=Service("C:\web drivers selenium\chromedriver_win32\chromedriver.exe")
Driver=webdriver.Chrome(service=serv_obj)

Driver.get('https://www.moneycontrol.com/fixed-income/calculator/hsbc/fixed-deposit-calculator-ZZZ-BHS001.html?classic=true')

file="C:\selenium web drivers\New Microsoft Excel Worksheet new.xlsx"

rows=xlutils.GetRowCount()

for r in range(1,rows+1):
    princ=xlutils.ReadData(file,"Sheet1",r,1)
    

