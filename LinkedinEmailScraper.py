'''
TO DO:
1. Scrape email from profile who has it
'''

import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

#login page from chrome: must download chromedriver
browser = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

#read login info from text file config.txt
file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

#enter login info
elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

#find desired profile to scrape
visitingProfileID = ['in/siningchen/']
for profile in visitingProfileID:
    fulllink = 'https://www.linkedin.com/' + profile
    browser.get(fulllink)

    #scroll through page in order to obtain all data
    SCROLL_PAUSE_TIME = 5

    last_height = browser.execute_script('return document.body.scrollHeight')
    for i in range(3):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script('return document.body.scrollHeight')
        last_height = new_height

    #obtain page source and ability to scrape
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

    contacts = soup.find('a', {'data-control-name': "contact_see_more"}).get("href")
    browser.get("https://www.linkedin.com" + contacts)

    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

    contact = soup.find_all('a', {'class' : "pv-contact-info__contact-link t-14 t-black t-normal"})
    email = contact[-1].get_text().strip()

    email_list = open("EmailList", "a")
    email_list.write(email)
    email_list.close()