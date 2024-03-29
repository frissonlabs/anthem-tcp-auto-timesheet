from os import getenv
from dotenv import load_dotenv

from pathlib import Path  # Python 3.6+ only
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from time import sleep

options = Options()
# options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

from login import handle_login_page, wait_until_logged_in
from timesheet import fill_timesheet, submit_timesheet, get_timesheet_date_range

try:
	print("Logging in...")
	# handle_login_page(driver, getenv("TCP_URL"), getenv("TCP_USERNAME"), getenv("TCP_PASSWORD"))
	driver.get(getenv("TCP_URL"))
	wait_until_logged_in(driver)

	print("Successfully logged in!")
	date_range = get_timesheet_date_range(driver)
	print("Starting timesheet submission for " + date_range)
	# if can_submit_timesheet(driver):
	fill_timesheet(driver, getenv("TCP_PROJECT_ID"))
	submit_timesheet(driver)
	print("Timesheet submitted for " + date_range)
	# else:
	# 	print("Timesheet already submitted for " + date_range)
except Exception as e:
	print(e)
	exit()

driver.close()
