#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 10 22:15:08 2019

@author: manzars
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.margma.com.my/ordinary-members/"

req = requests.get(url)
soup = BeautifulSoup(req.text, 'lxml')

div = soup.findAll('div', {'id': 'az-slider'})
lis = div[0].findAll('li')
links = []
for li in lis:
    links.append(li.a.attrs['href'])
    
header = "Company Name, Telephone, Fax, Email, Website\n"
file = open('assignment.csv', 'w')
file.write(header)
for link in links:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'lxml')
    name = soup.findAll('div', {'class': 'section-title blog-title'})[0].findAll('h1')[0].text
    #print(name)
    td = soup.findAll('td')[1::2][2:6]
    tel = td[0].text
    fax = td[1].text
    try:
        email = td[2].a.attrs['href'].split('mailto:')[1]
    except:
        email = td[2].text
    try:
        web = td[3].a.attrs['href']
    except:
        web = td[3].text
    print(name, tel, fax, email.replace('\n', ' | '), web.replace('\n', ' | '))
    file.write(name.replace(',', '').replace('\n', '') + ', ' + tel.replace(',', '').replace('\n', '') + ', ' + fax.replace(',', '').replace('\n', '') + ', ' + email.replace('\n', ' | ').replace(',', '') + ', ' + web.replace('\n', ' | ').replace(',', '') + '\n')
file.close()

    