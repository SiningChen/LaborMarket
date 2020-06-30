'''
TO DO:
1. Click intercepted by messaging pop-up
2. Save data to txt file
3. Track data daily

Note: Job postings are in Canada

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


browser.get('https://www.linkedin.com/jobs/?showJobAlertsModal=false')

job_list = ['computer support technician', 'digital marketer', 'front-end developer', 'security specialist', 'ml engineer', 'marketing analyst', 'hr analyst', 'software engineer', 'data scientist']
job_postings = {}

jobID = browser.find_element_by_id('jobs-search-box-keyword-id-ember19')
for job in job_list:
    jobID.send_keys(job)
    search = browser.find_element_by_class_name('jobs-search-box__submit-button')
    search.click()

    src = browser.page_source
    soup = BeautifulSoup(src, 'lxml')

    results = soup.find('div', {'class' : 'jobs-search-two-pane__title-heading'})
    results = int(results.find('small', {'class' : 'display-flex'}).get_text().strip().split()[0])

    job_postings[job] = results

print(job_postings)