'''
Author: Vishal K (vkmaxcooldude)
Python 3
Using the BeautifulSoup and requests Python packages to print out a list of all the article titles, link and Summary
on the New York Times homepage.
Install BeautifulSoup, requests and lxml parser using pip cmd installer
'''
from bs4 import BeautifulSoup
import requests
while True:
    r = requests.get("https://www.nytimes.com/index.html")
    if r.status_code == requests.codes.ok:
        break
r_html = r.text
soup = BeautifulSoup(r_html, 'lxml')
#print(soup.prettify())
title = soup.find_all('article')
for x in title:
    try:
        print()
        link = x.a['href']
        print("HEADLINE: " + x.a.h2.text)
        print("   Link: https://www.nytimes.com" + str(link))
        try:
            ordered_list = x.find('ul')
            ctr = 0
            for y in ordered_list:
                ctr += 1
                print("   " + str(ctr) + ". " + y.text)
        except:
            print("   " + x.a.p.text)
    except:
        continue

    print()
for x in title:
    try:
        print()
        link = x.a['href']
        print("HEADLINE: " + x.a.h2.span.text)
        print("   Link: https://www.nytimes.com" + str(link))
        try:
            ordered_list = x.find('ul')
            ctr = 0
            for y in ordered_list:
                ctr += 1
                print("   " + str(ctr) + ". " + y.text)
        except:
            print("   " + x.a.p.text)
    except:
        continue
    print()
