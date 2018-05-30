#! /usr/bin/env python
# coding: utf-8

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver',
                          chrome_options=chrome_options)
driver.get('http://news.joins.com/DigitalSpecial/298')
sel1 = driver.find_element_by_id('selDepth1')
#it can't use click method : https://stackoverflow.com/questions/27927964/selenium-element-not-visible-exception?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#sel1.click()
driver.execute_script("document.querySelectorAll('#selDepth1')[0].click()")
sel1_items = sel1.find_elements_by_xpath('div//div')

# skip first item
for pos1, item1 in enumerate(sel1_items[1:], 1):
    #item1.click()
    driver.execute_script("document.querySelectorAll('#selDepth1 > div > div')[" + str(pos1) + "].click()")
    item1text = item1.get_attribute('innerHTML')
    sel2 = driver.find_element_by_id('selDepth2')
    #sel2.click()
    driver.execute_script("document.querySelectorAll('#selDepth2')[0].click()")
    sel2_items = sel2.find_elements_by_xpath('div//div')
    for pos2, item2 in enumerate(sel2_items[1:], 1):
        #item2.click()
        driver.execute_script("document.querySelectorAll('#selDepth2 > div > div')[" + str(pos2) + "].click()")
        item2text = item2.get_attribute('innerHTML')
        try:
            mostused = driver.find_element_by_class_name('col10')
        except NoSuchElementException:
            mostusedtext = 'N/A'
        else:
            mostusedtext = mostused.get_attribute('innerHTML')
        finally:
            print item1text, item2text, mostusedtext

driver.quit()
