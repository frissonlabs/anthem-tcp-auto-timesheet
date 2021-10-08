from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

from os import getenv
from dotenv import load_dotenv

from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

def handle_login_page(webdriver: WebDriver, url, username, password, one_time_passcode = None) -> None:
	webdriver.get(url)

	wait = WebDriverWait(webdriver, 30)

	sleep(3)
	wait.until(
		lambda x: x.find_element_by_xpath('//input[@id="username"]').is_displayed()
	)
 
	login_field = wait.until(lambda driver: driver.find_element_by_xpath('//input[@id="username"]'))
	password_field = wait.until(lambda driver: driver.find_element_by_xpath('//input[@id="password"]'))

	if not login_field.text:
		login_field.clear()
		login_field.send_keys(username)
		password_field.clear()
		password_field.send_keys(password)
	
	submit_button = wait.until(
		lambda x: x.find_element_by_xpath('//a[@title="Submit"]')
	)

	submit_button.click()
 
	return wait.until(
		lambda x: x.find_element_by_xpath('//span[contains(text(),\'Time Sheet Portal\')]')
	)

		
