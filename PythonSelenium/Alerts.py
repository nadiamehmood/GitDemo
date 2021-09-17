#Handle javascript alerts
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')

driver.find_element_by_id("name").send_keys("Nadia")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
assert 'Nadia' in alert.text
#alert.accept()     # when you want to click on ok button
alert.dismiss()
# driver.find_element_by_id("name").send_keys("Mehmood")
# driver.find_element_by_id("confirmbtn").click()
# alert2 = driver.switch_to.alert
# alert2.dismiss()