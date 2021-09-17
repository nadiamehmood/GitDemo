import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://www.makemytrip.com/')

driver.find_element_by_id("fromCity").click()
#driver.find_element_by_css_selector("input[placeholder='From']").send_keys("Lahore")
#cities = driver.find_elements_by_css_selector("p[class='blackText']")
# for city in cities:
#     if "Lahore" in city.text:
#         city.click()
#         break
# print("Textfield text is: "+ driver.find_element_by_id("fromCity").get_attribute('value'))