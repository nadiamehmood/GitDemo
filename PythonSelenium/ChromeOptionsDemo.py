# what are chrome options and importance of them in selenium
# Link: https://www.programcreek.com/python/example/100025/selenium.webdriver.ChromeOptions

from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument("--start-maximized")
# chromeOptions.add_argument("headless")
chromeOptions.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(executable_path=r'C:\Users\Southville\Downloads\chromedriver_win32\chromedriver', options=chromeOptions)
driver.get('https://rahulshettyacademy.com/angularpractice/')

print(driver.title)