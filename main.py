from selenium import webdriver
from selenium.webdriver.chrome.service import Service # may be needed later
from selenium.webdriver.chrome.options import Options # may be needed later
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# set up path to chrome driver
PATH = r"C:\Program Files (x86)\chromedriver.exe"

# site URL to be loaded
page_url = "https://localhost:7095/"

# create an instance of the chrome driver
driver = webdriver.Chrome()

# open the web page
driver.get(page_url)

# locate the product element and click on it
try:
    #  finds all <a> tags and searches for elements whose href attribute contain 'Product/Details/1' 
    product_Element = driver.find_element(By.XPATH, "//a[contains(@href, 'Product/Details/1')]") 
    product_Element.click()
    add_category_link = driver.find_element(By.LINK_TEXT, "Add Category")
    add_category_link.click()
   # find all elements with the link text "Add"
    add_buttons = driver.find_elements(By.LINK_TEXT, "Add")
    add_buttons[2].click()

    
    print("Shirt clicked successfully.")

  # wait until the Assign button is clickable and then click it
    assign_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clicked((By.XPATH, "//input[@value='Assign']"))
    )
    assign_button.click()
    time.sleep(60)
except Exception as e:
    print(f"An error occurred: {e}")

# close the browser

driver.quit()
