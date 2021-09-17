from selenium import webdriver

#driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver')
#driver = webdriver.Firefox(executable_path=r'C:\Users\Southville\Downloads\geckodriver-v0.27.0-win64\geckodriver')
driver = webdriver.Ie(executable_path=r'C:\Users\Southville\Downloads\IEDriverServer_x64_3.150.1\IEDriverServer')
driver.get('https://rahulshettyacademy.com/#/index')         # http://206.189.237.25/
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get('https://rahulshettyacademy.com/#/index')
print(driver.title)
print(driver.current_url)
driver.back()
driver.refresh()
driver.minimize_window()
driver.close()   # only the current window will close
#driver.quit()    # all the windows which are open will close simultanuously