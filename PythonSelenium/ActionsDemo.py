from selenium import webdriver
from selenium.webdriver import ActionChains

# -----------------hover on button and click on dropdown element--------------------
driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://www.rahulshettyacademy.com/AutomationPractice/')
driver.implicitly_wait(5)
action = ActionChains(driver)
menuBtn = driver.find_element_by_id("mousehover")
action.move_to_element(menuBtn).perform()
reload = driver.find_element_by_link_text("Reload")
action.move_to_element(reload).click().perform()

# -----------------------Double click the button----------------------
driver.get('https://chercher.tech/practice/practice-pop-ups-selenium-webdriver')
actions = ActionChains(driver)
actions.context_click(driver.find_element_by_id("double-click")).perform()  # when you want to right click on any object
actions.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()

