from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.amazon.in')

driver.maximize_window()

# Finding element by path
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('iphones')

driver.find_element_by_xpath("//input[@id='nav-search-submit-button']").click()

# Getting data
list = driver.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")

# listing products found
print(str(len(list)) + ' products found')

for i in list:
    print(i.text)

time.sleep(30)
driver.quit()
