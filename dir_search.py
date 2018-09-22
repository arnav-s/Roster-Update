import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_dir_res():
    url = 'https://www.wisc.edu/directories/'

    driver = webdriver.Firefox()

    wp = driver.get(url)

    main_el = driver.find_element_by_id('main')

    element = main_el.find_element_by_name('q')



    element.click()

    element.send_keys('Arnav Sharma ')

    people = main_el.find_element_by_id('people')
    for i in range(3):
        try:
            emails = people.find_elements_by_class_name('person_email')
            e = [email.text for email in emails]
        except:
            continue

    return e
