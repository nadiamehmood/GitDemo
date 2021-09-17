# Selecting a product from list of products with product name parameter
# and complete checkout logic with product selection
# Handle auto suggestive dropdown to select location and confirm order
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://rahulshettyacademy.com/angularpractice/shop')
driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
device = "Blackberry"

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    print(product.find_element_by_xpath("div/h4/a").text)
    if product.find_element_by_xpath("div/h4/a").text == device:
        print("Blackberry card detected")
        # Add item into the cart
        product.find_element_by_xpath("div/button").click()

buttonCheck = driver.find_element_by_css_selector(".btn-primary").text
assert "1" in buttonCheck

driver.find_element_by_css_selector(".btn-primary").click()
driver.find_element_by_xpath("//tr/td[2]/input").clear()
driver.find_element_by_xpath("//tr/td[2]/input").send_keys("2")
assert "100000" in driver.find_element_by_xpath("//tr/td[4]/strong").text

driver.find_element_by_css_selector(".btn-success").click()
# Add delivery country
driver.find_element_by_id("country").send_keys("Pa")
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Pakistan")))
driver.find_element_by_link_text("Pakistan").click()
assert driver.find_element_by_id("country").get_attribute('value') == "Pakistan"
driver.find_element_by_css_selector("label[for='checkbox2']").click()
driver.find_element_by_css_selector(".btn-lg").click()

successMsg = driver.find_element_by_css_selector(".alert").text
print(successMsg)
assert "Success" in successMsg

driver.get_screenshot_as_file("screen.png")
