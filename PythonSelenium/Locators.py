from selenium import webdriver
# ID  ==> find_element_by_id("idName")
# Regular expression for id => tagname#id
# Name  ==> find_element_by_name("name")
# CCS Selector  ==>find_element_by_css_selector("TagName[attribute='value']")        VERY VERY FAST LOCATOR
# Regular expression for css selector => [Tagname*(attribute='value')]
# Generating css by id ==> find_element_by_css_selector("#idName")
# Generating css by class name ==> (".ClassName")    #make sure there are no spaces in class name. Replace with .
# Xpath  ==> find_element_by_XPath("//TagName[@attribute='value']")
# Generating xpath based on text ==> find_element_by_XPath("//TagName[text()='value']")
# Regular expression for XPath => //*[contains(@attribute, 'value')]
# Creating css and xpath by traversing tags => Xpath then tagname => //tagname[@attribute='value']/tagname => ParentTag/ChildTag
# Creating css and xpath by traversing tags => CSS then tagname => tagname[attribute='value'] tagname => ParentTag ChildTag
# ClassName  ==> find_element_by_class_name("class name")
# LinkText ==> find_element_by_link_text("Link text")    #tagname must be "a" because it indicates the link tag
# tagName ==>
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://rahulshettyacademy.com/angularpractice/')
#driver.find_element_by_name("name").send_keys("Nadia")       # By Name
driver.find_element_by_css_selector("input[name='name']").send_keys(" Mehmood")    # CCS Selector
driver.find_element_by_name("email").send_keys("nadiamehmood66@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("nadia@123")       # By id
driver.find_element_by_id("exampleCheck1").click()
# Select class provide the methods to handle the options in dropdown
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0)

driver.find_element_by_xpath("//input[@type='submit']").click()        # By xpath
message = driver.find_element_by_class_name("alert-success").text  # there are 3 classes in this field "alert", "alert-success", "alert-dismissible" so pick only 1 class
print("message"+message)
assert "successs" in message

driver.get('https://login.salesforce.com/?locale=eu')
driver.find_element_by_css_selector("#username").send_keys("nadiamehmood66")     # Generating css by id
driver.find_element_by_css_selector(".password").send_keys("nadia@123")
driver.find_element_by_css_selector(".password").clear()        # Generating css by class name
driver.find_element_by_link_text("Forgot Your Password?").click()    # By Link Text
driver.find_element_by_xpath("//a[text()='Cancel']").click()    # Generating xpath based on text
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)  # Creating css and xpath by traversing tags => Xpath then tagname
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(4)").text)  # Creating css and xpath by traversing tags => CSS then tagname

# Difference between relative xpath and absolute xpath:
# Absolute XPath: Generating xpath from the root of the html
# Relative XPath: will directly target that particular element.
# Relative xpath is better
