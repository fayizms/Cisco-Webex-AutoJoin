from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time

NAME = "8C Fayis 7"
EMAIL = "sfayizmuhammed@gmail.com"
s_id = input("Enter session id: ")
s_pwd = input("Enter session password")

driver = webdriver.Chrome()
driver.get(
    "https://stthomasschools.webex.com/mw3300/mywebex/default.do?service=7&siteurl=stthomasschools&main_url=%2Ftc3300%2Ftrainingcenter%2Fdefault.do%3Fsiteurl%3Dstthomasschools%26main_url%3D%252Ftc3300%252Ftrainingcenter2%252Fsite%252Flandingpage.do%253Fsiteurl%253Dstthomasschools"
)

attend = driver.find_element_by_id("wcc-lnk-attendASession")
attend.click()
time.sleep(0.5)

id_input = driver.find_element_by_id("TrackNum")
id_input.send_keys(s_id)
id_input.send_keys(Keys.RETURN)
time.sleep(0.5)

pwd_input = driver.find_element_by_name("password")
pwd_input.send_keys(s_pwd)
pwd_input.send_keys(Keys.RETURN)

try:
	name_field = WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(By.ID, "join.label.userName"))
	email_field = driver.find_element_by_id("join.label.emailAddress")
	pwd_field = driver.find_element_by_id("join.label.password")

	name_field.send_keys(NAME)
	email_field.send_keys(EMAIL)
	pwd_field.send_keys(s_pwd)

	join = driver.find_element_by_name("joinnow")
	join.click()

	time.sleep(5)

finally:
	driver.close()
