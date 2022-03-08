from pathlib import Path
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from dotenv import load_dotenv
import os
import time


dotenv_path = Path(".env")
load_dotenv(dotenv_path=dotenv_path)

USER = os.getenv("USER")
PASSWORD = os.getenv("PASSWORD")
PHONE = os.getenv("PHONE")

chrome_driver = "C:\Developer\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get("""https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20
England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0""")

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

account = driver.find_element_by_id("username")
account.send_keys(USER)

password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(3)

apply_now = driver.find_element_by_css_selector(".jobs-apply-button--top-card button")
apply_now.click()

add_phone = driver.find_element_by_css_selector(".display-flex input")
add_phone.send_keys(PHONE)

next = driver.find_element_by_css_selector(".jobs-easy-apply-content button")
next.click()

next_2 = driver.find_element_by_css_selector(".jobs-easy-apply-content button")
next_2.click()