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

    messaging = browser.find_element_by_class_name('msg-overlay-bubble-header')
    messaging.click()

    messages = soup.find('span', {'id' : 'ember59'}).find('a', {'class': "message-anywhere-button"}).get("href")

    browser.get("https://www.linkedin.com" + messages)

    # obtain page source and ability to scrape
    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

    message = "Hi, this is a test message"

    text_box = browser.find_element_by_class_name('msg-form__contenteditable')
    text_box.send_keys(message)
    text_box.submit()