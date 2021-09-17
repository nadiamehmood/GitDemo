# JS DOM can access any element on a web page just like how selenium does
# selenium have a method to execute javascript code in it
# How we scroll in selenium?
# Selenium By default do not have the ability to scroll so we reply on javascript executor or js methods to do that

from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://rahulshettyacademy.com/angularpractice/')

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute('value'))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopBtn = driver.find_element_by_css_selector("a[href='/angularpractice/shop']")
# purely javascript, we use this when we have a view above this button
driver.execute_script("arguments[0].click();", shopBtn)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")

