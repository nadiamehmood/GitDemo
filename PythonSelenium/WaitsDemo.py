# Implicit Wait
# Explicit Wait
# Pause the screen for few seconds with time class
# When to use explicit wait? -> When you think your application is super fast and there are only 2 to 3
# areas which require loading then go for explicit wait
# When to use implicit wait? -> when you environment is slow or having inconsistency it all depends on how many
# users are using the application in 1 particular time then use implicit wait and give maximum wait globally.

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

page1ProductNames = []
page2ProductNames = []
sum = 0

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://www.rahulshettyacademy.com/seleniumPractise/#/')
driver.implicitly_wait(5)
# Implicit wait
# Global Wait
# wait until 5 seconds if object is not displayed
# 1.5 second to reach next page - execution will resume in 1.5 seconds
# if object do not show up at all then max time your test waits for 5 seconds
driver.find_element_by_css_selector("input[type='search']").send_keys("ber")
driver.find_element_by_css_selector("button[type='submit']").click()
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
print("{} {}".format("Product cards length", len(products)))
productButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print("{} {}".format("Product Buttons length", len(productButtons)))

for productButton in productButtons:
    page1ProductNames.append(productButton.find_element_by_xpath("parent::div/parent::div/h4").text)
    productButton.click()
print(page1ProductNames)
# ------------------------Verify searching is working or not-------------------
for searchValue in page1ProductNames:
    print("{} {}".format("search value: ", searchValue))
    assert "ber" in searchValue

driver.find_element_by_xpath("//img[@alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    page2ProductNames.append(veg.text)
print(page2ProductNames)
# ----------------Validate page 1 products matches with page 2--------------------
assert page1ProductNames == page2ProductNames

priceList = driver.find_elements_by_xpath("//tr/td[5]/p")
for price in priceList:
    sum = sum + int(price.text)
    print(sum)

AmountBeforeDiscount = driver.find_element_by_css_selector("span.discountAmt").text
# ------------------------Validate sum of all products equal to total amount-----------------
assert sum == int(AmountBeforeDiscount)

driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
# explicit wait:
# it will wait until the targeted element reached
AmountAfterDiscount = driver.find_element_by_css_selector("span.discountAmt").text

# ----------------Validate whether amount decreased or not after discount---------------------
assert float(AmountAfterDiscount) < int(AmountBeforeDiscount)

print(driver.find_element_by_css_selector("span.promoInfo").text)
#assert "code applied" in driver.find_element_by_css_selector("span.promoInfo").text

