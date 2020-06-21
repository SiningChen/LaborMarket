import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
from bs4 import BeautifulSoup

browser = webdriver.Chrome('chromedriver_win32/chromedriver.exe')

browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

file = open('config.txt')
lines = file.readlines()
username = lines[0]
password = lines[1]

elementID = browser.find_element_by_id('username')
elementID.send_keys(username)

elementID = browser.find_element_by_id('password')
elementID.send_keys(password)

elementID.submit()

visitingProfileID = 'in/rishabh-singh-61b706114/'
fulllink = 'https://www.linkedin.com/' + visitingProfileID
browser.get(fulllink)

SCROLL_PAUSE_TIME = 5

last_height = browser.execute_script('return document.body.scrollHeight')
for i in range(3):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = browser.execute_script('return document.body.scrollHeight')
    last_height = new_height

src = browser.page_source

soup = BeautifulSoup(src, 'lxml')

name_div = soup.find('div', {'class' : 'flex-1 mr5'})

name_loc = name_div.find_all('ul')
name = name_loc[0].find('li').get_text().strip()
loc = name_loc[1].find('li').get_text().strip()

profile_title = name_div.find('h2').get_text().strip()

connection = name_loc[1].find_all('li')
connection = connection[1].get_text().strip()

info = []
info.append(name)
info.append(profile_title)
info.append(loc)
info.append(connection)

exp_section = soup.find('section', {'id' : 'experience-section'})

exp_section = exp_section.find('ul')
li_tags = exp_section.find('div')
a_tags = li_tags.find('a')

job_title = a_tags.find('h3').get_text().strip()
company_name = a_tags.find_all('p')[1].get_text().strip()
joining_date = a_tags.find_all('h4')[0].find_all('span')[1].get_text().strip()
exp = a_tags.find_all('h4')[1].find_all('span')[1].get_text().strip()

info.append(company_name)
info.append(job_title)
info.append(joining_date)
info.append(exp)

print(info)