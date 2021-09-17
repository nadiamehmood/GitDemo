# Handling Auto Suggestive dynamic dropdowns
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')

driver.find_element_by_id("autosuggest").send_keys("Aus")
time.sleep(2)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print("{} {}".format("Length of Drop down is: ", len(countries)))
for country in countries:
    if country.text == "Austria":
        country.click()
        break
print("Text "+ driver.find_element_by_id("autosuggest").get_attribute('value'))
assert driver.find_element_by_id("autosuggest").get_attribute('value') == 'Austria'  # Get value directly from dom
# assert will always expect the statement becomes true if no then it will raise an exception
