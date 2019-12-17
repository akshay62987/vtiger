from selenium import webdriver
import time

from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://localhost:8888/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element_by_name("user_name").send_keys("admin")
driver.find_element_by_name("user_password").send_keys("manager")
driver.find_element_by_id("submitButton").click()
time.sleep(3)
driver.find_element_by_xpath("//a[text()='Organizations']").click()
driver.find_element_by_xpath("//img[@title='Create Organization...']").click()
#Enter form details
driver.find_element_by_name("accountname").send_keys("Python")
select = driver.find_element_by_name("industry")
a = Select(select)
a.select_by_visible_text("Technology")

driver.find_element_by_xpath("//input[@value='  Save  ']").click()
Org_No = driver.find_element_by_xpath("//span[@class='dvHeaderText']")
print(Org_No.text)