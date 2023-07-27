from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/workspace/Gitpod-Projects/qsale/chromedriver_win32/chromedriver.exe')

service.start()

driver = webdriver.Remote(service.service_url)

driver.get('http://www.google.com/');

input("Press Enter key to quit")

driver.quit()