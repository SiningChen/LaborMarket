'''
TO DO:
x Click intercepted by messaging pop-up
x Save data to txt file
3. Track data daily

Note: Job postings are in Canada

'''

import os, random, sys, time
from datetime import date
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

job_list = ['computer support technician', 'digital marketer', 'front-end developer', 'security specialist', 'ml engineer', 'marketing analyst', 'hr analyst', 'software engineer', 'data scientist']
job_postings = {}
message_click = True

for job in job_list:
    #Access job
    browser.get('https://www.linkedin.com/jobs/?showJobAlertsModal=false')
    jobID = browser.find_element_by_id('jobs-search-box-keyword-id-ember17')
    jobID.send_keys(job)
    if message_click:
        messaging = browser.find_element_by_class_name('msg-overlay-bubble-header')
        messaging.click()
        message_click = False
    search = browser.find_element_by_class_name('jobs-search-box__submit-button')
    search.click()

    SCROLL_PAUSE_TIME = 5

    #Could condense, not sure of function
    last_height = browser.execute_script('return document.body.scrollHeight')
    for i in range(3):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = browser.execute_script('return document.body.scrollHeight')
        last_height = new_height

    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

    results = soup.find('small', {'class': 'display-flex t-12 t-black--light t-normal'}).get_text().strip().split()[0]
    results = int(results.replace(',', ''))

    job_postings[job] = results
    today = date.today()
    data = open("JobPostingsData", "a")
    data.write("%s %s %s\n" % (today, job, results))
    data.close()
