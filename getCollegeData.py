import os
import requests
import bs4 as bs
import csv
import re
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

#create webdriver
#driver = webdriver.Chrome(r"C:\Users\CommandCenter\AppData\Local\Programs\Python\Python36-32\chromedriver.exe")
driver = webdriver.Chrome(r"C:\Program Files\Python\Python36\chromedriver.exe")

with open("collegeBoard.csv") as csvfileA:
    reader = csv.DictReader(csvfileA)
    with open('Result.csv', 'a') as csvfileB:
        fieldnames = ['Result']
        writer = csv.DictWriter(csvfileB, fieldnames=fieldnames, lineterminator = '\n')
        writer.writeheader()
        for row in reader:
            collegeRawName = (row['College'])
            collegeURL = collegeRawName.replace(" ","-")
            driver.get('https://bigfuture.collegeboard.org/college-university-search/' + collegeURL)
            time.sleep(1)
            try:
                CollegeName = driver.find_element_by_xpath('//*[@id="titleFrame"]/div/div[1]/h1')
                writer.writerow({'Result': CollegeName.text})
            except NoSuchElementException:
                writer.writerow({'Result': "ERROR: " + collegeRawName})
