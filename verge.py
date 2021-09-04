from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="C:/Users/ASUS/AppData/Local/Programs/Python/Python39/chromedriver.exe", chrome_options=options)
driver.get("https://www.theverge.com/")
sleep(2)




# contents = driver.find_elements_by_class_name('c-entry-box--compact c-entry-box--compact--article c-entry-box--compact--hero')
# for content in contents:
#     href =content.get_attribute('href')
#     print(href)


contents = driver.find_elements_by_class_name('c-entry-box--compact__image-wrapper')
for content in contents:
    href =content.get_attribute('href')
    print(href)


# links = driver.find_elements_by_tag_name('h2')
# for link in links:
#     print (link)



# div = driver.find_element_by_class_name('c-entry-box--compact__title')
# links = div.find_element_by_css_selector('a').get_attribute('href')
# print (links)



# for link in links:      
#     print(link)
# contents = driver.find_elements_by_class_name('c-seven-up')
# for content in contents:
#     href =content.get_attribute('href')
#     print(href)

# elems = driver.find_elements_by_tag_name('a')
# for elem in elems:
#     href = elem.get_attribute('href')
#     if href is not None:
#         print(href)
driver.close()