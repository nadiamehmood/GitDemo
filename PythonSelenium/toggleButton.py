from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
driver.maximize_window()
driver.get('https://jqueryui.com/slider/')
driver.switch_to.frame(0)
slider = driver.find_element_by_xpath("//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
# slider_min_value = driver.find_element_by_xpath("//span[contains(@class, )]")
# //span[ contains(@class, 'slider-min')]
action = ActionChains(driver)
action.click_and_hold(slider).move_by_offset(100, 0).pause(4).move_by_offset(-20, 0).release().perform()