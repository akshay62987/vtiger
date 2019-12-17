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
select = driver.find_element_by_id("qccombo")
a = Select(select)
a.select_by_visible_text("New Organization")
time.sleep(2)
driver.find_element_by_name("accountname").send_keys("Fish")
driver.find_element_by_xpath("//input[@value='T']").click()
driver.find_element_by_name("button").click()