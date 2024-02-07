from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import pandas as pd
import time

driver = webdriver.Chrome()
# Set up the Chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')
time.sleep(1)
driver.set_window_position(0, 0)
driver.maximize_window()
time.sleep(1)
driver.get('https://www.industrynet.com/suppliers/FA0280/farm-equipment')


def featured_suppliers ():
    elements = driver.find_elements(By.XPATH, '//td[contains(@class,"supplierresultstd2")]/div[contains(@class,"header4font")]')
    for element in elements:
        print(element.text)    

def preferred_suppliers():
    elements = driver.find_elements(By.XPATH, '//td[contains(@class,"supplierresultspreftd1")]/div[contains(@class,"header4font")]')
    for element in elements:
        print(element.text)

def other_suppliers():
    elements = driver.find_elements(By.XPATH, '//td[contains(@class,"supplierresultsfreetd1")]/div[contains(@class,"bodyfont")]/a')
    for element in elements:
        print(element.text)

def next_page():
    try:
        next_button = driver.find_element(By.XPATH, '//a/span[contains(text(),"Next")]')
        next_button.click()
    except:
        print("No more pages")




number_of_pages = int(input("Enter the number of pages you want to scrape: "))
print("--------------------------------------------------------")
print("Featured Suppliers")
featured_suppliers()
print("--------------------------------------------------------")
print("Preferred Suppliers")
preferred_suppliers()
print("--------------------------------------------------------")
print("Other Suppliers")
for i in range(number_of_pages):
    other_suppliers()
    next_page()
    time.sleep(2)

driver.quit()
