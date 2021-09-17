import time

from selenium import webdriver

# 3 types of frames: iframe.frameset, frame
# developer either define frame id, frame name or frame index
driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.get('https://the-internet.herokuapp.com/iframe')
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("New Text")
# this is the method which will bring you back to the normal browser
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
assert "An iFrame containing the TinyMCE WYSIWYG Editor" == driver.find_element_by_tag_name("h3").text
time.sleep(3)
driver.close()
