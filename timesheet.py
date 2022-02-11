from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

def fill_timesheet(webdriver, project_id) -> None:
	wait = WebDriverWait(webdriver, 30)

	add_project_button = webdriver.find_element_by_xpath('//a[contains(text(),\'' + project_id + '\')]/following-sibling::button[contains(text(), "Add to Time Sheet")]')
	add_project_button.click()

	project = wait.until(lambda x: x.find_element_by_xpath("//div[@ng-dblclick='editRow($event, item);']"))
	actions = ActionChains(webdriver)
	actions.double_click(project).perform()

	project_phase = wait.until(lambda x: x.find_element_by_xpath("//select[@id='u_project_phase']"))
	Select(project_phase).select_by_value('string:initiate')

	sleep(3)

	for day in days:
		input = webdriver.find_element_by_xpath("//input[@id=\'" + day + "']")
		input.send_keys(8)

	more_actions_button = webdriver.find_element_by_xpath("//a[@aria-label='More Actions']")
	more_actions_button.click()

	submit_button = webdriver.find_element_by_xpath("//a[contains(text(),'Submit Time Card')]")
	submit_button.click()

def submit_timesheet(webdriver) -> None:
	webdriver.find_element_by_xpath("//button[@ng-click='submitTimesheet($event)']").click()
 
def get_timesheet_date_range(webdriver) -> str:
	try:
		date_range: WebElement = WebDriverWait(webdriver, 30).until(
			lambda x: x.find_element_by_xpath('//div[@id="datetimepicker_timesheet"]')
		)
		print(date_range)
		return date_range.find_element_by_tag_name('span').text
	except Exception:
		return "?"
