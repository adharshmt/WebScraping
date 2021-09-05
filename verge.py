from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)

driver.get("https://www.theverge.com/")
sleep(2)

f=open('verge.html','a+')
f.write("<html>\n<body>\n<h2>Verge Main News</h2>\n")
main_seven = driver.find_elements_by_class_name('c-seven-up__main')

for main_news in main_seven:
    single_news = main_news.find_elements_by_class_name('c-entry-box--compact')
    for news in single_news:
        picturetag = news.find_element_by_tag_name('picture')
        picturesource = picturetag.find_element_by_tag_name('source')
        picture = picturesource.get_attribute('srcset')
        picturelink = (picture.split(" ",1)[0])
        singlenewsfull = news.find_element_by_class_name('c-entry-box--compact__title')
        taginsingle = singlenewsfull.find_element_by_tag_name('a')
        href = taginsingle.get_attribute('href')
        linktext=taginsingle.text
        f.write("<p><a href=\""+str(href)+"\">"+str(linktext)+"</a></p>\n")
        f.write("<img src=\""+str(picturelink)+"\"  width=\"200\" height=\"142\">\n")
f.close()
driver.close()