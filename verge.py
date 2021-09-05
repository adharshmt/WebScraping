from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get("https://www.theverge.com/")
sleep(2)


main_seven = driver.find_elements_by_class_name('c-seven-up__main')
for main_news in main_seven:
    single_news = main_news.find_elements_by_class_name('c-entry-box--compact')
    for news in single_news:
        picturetag = news.find_element_by_tag_name('picture')
            picturesource = picturetag.find_element_by_tag_name('source')
                picture = picturesource.get_attribute('srcset')
                print(picture.split(" ",1)[0])
                print('\n')
        singlenewsfull = news.find_element_by_class_name('c-entry-box--compact__title')
            taginsingle = singlenewsfull.find_element_by_tag_name('a')
                href = taginsingle.get_attribute('href')
                print(taginsingle.text)
                print('\n')
                print(href)


driver.close()
