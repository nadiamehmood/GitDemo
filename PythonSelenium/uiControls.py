
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')

checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")

for checkbox in checkboxes:
    value = checkbox.get_attribute('value')
    if value == 'option2':
        checkbox.click()
    #print(checkbox.is_selected())
    #assert checkbox.is_selected()

radiobtns = driver.find_elements_by_xpath("//input[@type='radio']")
radiobtns[2].click()
# OR
# for radiobtn in radiobtns:
#     print(radiobtn.get_attribute('value'))
#     if radiobtn.get_attribute('value') == 'radio2':
#         radiobtn.click()
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()