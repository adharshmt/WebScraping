from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get("https://www.theverge.com/")
sleep(2)


contents = driver.find_elements_by_class_name('c-entry-box--compact__title')
for content in contents:
    elem = content.find_element_by_tag_name('a')
    href = elem.get_attribute('href')
    print(elem.text)
    print(href)
    print()


driver.close()
