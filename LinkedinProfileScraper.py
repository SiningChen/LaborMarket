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

    info = {}

    name_div = soup.find('div', {'class' : 'flex-1 mr5'})

    name_loc = name_div.find_all('ul')
    info['name'] = name_loc[0].find('li').get_text().strip()
    info['location'] = name_loc[1].find('li').get_text().strip()
    info['profile title'] = name_div.find('h2').get_text().strip()

    info['connection'] = name_loc[1].find_all('li')[1].get_text().strip()


    exp_section = soup.find('section', {'id' : 'experience-section'})
    # Try to condense
    if exp_section is not None:
        exp_section = exp_section.find('ul')
        if exp_section is not None:
            li_tags = exp_section.find_all('li')
            if li_tags is not None:
                for exp in range(len(li_tags)):
                    a_tags = li_tags[exp].find('a')
                    if a_tags is not None:
                        info['job title ' + str(exp+1)] = a_tags.find('h3').get_text().strip()
                        info['company name ' + str(exp+1)] = a_tags.find_all('p')[1].get_text().strip()
                        info['joining date ' + str(exp+1)] = a_tags.find_all('h4')[0].find_all('span')[1].get_text().strip()
                        info['experience ' + str(exp+1)] = a_tags.find_all('h4')[1].find_all('span')[1].get_text().strip()


    edu_section = soup.find('section', {'id': 'education-section'})
    if edu_section is not None:
        edu_section = edu_section.find('ul')
        if edu_section is not None:
            li_tags = edu_section.find_all('li')
            if li_tags is not None:
                for edu in range(len(li_tags)):

                    info['college name' + str(edu+1)] = li_tags[edu].find('h3').get_text().strip()

                    degree_name = li_tags[edu].find('p', {'class': 'pv-entity__secondary-title pv-entity__degree-name t-14 t-black t-normal'})
                    if degree_name is not None:
                        info['degree name' + str(edu+1)] = degree_name.find_all('span')[1].get_text().strip()

                    stream = li_tags[edu].find('p', {'class': 'pv-entity__secondary-title pv-entity__fos t-14 t-black t-normal'})
                    if stream is not None:
                        info['stream' + str(edu+1)] = stream.find_all('span')[1].get_text().strip()

                    degree_year = li_tags[edu].find('p', {'class': 'pv-entity__dates t-14 t-black--light t-normal'})
                    if degree_year is not None:
                        info['degree year' + str(edu+1)] = degree_year.find_all('span')[1].get_text().strip()


    print(info)