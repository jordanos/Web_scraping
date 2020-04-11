from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

"""
***READ THIS FIRST***

THIS IS A SIMPLE WEB SCRAPING SCRIPT FOR SCRAPING ALL PRODUCT INFO OF THIS
[https://www.janeiredale.co.uk/makeup] website.

ALL CELLS OF THE CSV FILE MUST BE FILLED WITH ? OR SOME VALUE FIRST.
ATLEAST 500 ROWS.

USE THE CSV I HAVE PROVIDED.

"""

YOUR-CSV-PATH =

driver = webdriver.Firefox()
df = pd.read_csv(YOUR-CSV-PATH)

ls = []
big_ls = []
ls_all = ['https://www.janeiredale.co.uk/face', 'https://www.janeiredale.co.uk/eyes-makeup',
        'https://www.janeiredale.co.uk/cheeks', 'https://www.janeiredale.co.uk/makeup-lips',
        'https://www.janeiredale.co.uk/tools-and-accessories', 'https://www.janeiredale.co.uk/more-skincare'
        ]


def scrap(cat, site, i):
    driver.get(site)
    time.sleep(5)

    attributes = driver.find_elements_by_xpath('//div[@class="productTabs-header"]//li[@role="tab"]')
    ltl_ls = []

    for att in attributes:
        ltl_ls.append(att.text)


    title = driver.find_element_by_xpath('//div[@class="product-name"]')
    df['Title'][i] = title.text

    cost = driver.find_element_by_xpath('//div[@class="product-price"]')
    df['Cost'][i] = cost.text

    try:
        short = driver.find_element_by_xpath('//div[@class="short-description"]')
        df['Short Description'][i] = short.text
    except Exception as e:
        pass


    for name in range(len(ltl_ls)):
        if ltl_ls[name].upper()  == 'DESCRIPTION' or ltl_ls[name].upper() == 'DETAILS':
            full = driver.find_element_by_xpath('//div[@aria-labelledby="ui-id-{}"]'.format(name+1))
            df['Long Description'][i] = full.text
        elif ltl_ls[name].upper() == 'INGREDIENTS':
            html = driver.find_element_by_xpath('//div[@aria-labelledby="ui-id-{}"]'.format(name+1)).get_attribute('innerHTML')
            ingredients = BeautifulSoup(html, 'lxml')
            df['INGREDIENTS'][i] = ingredients.text
        elif ltl_ls[name].upper() == 'CRUELTY FREE':
            html =  driver.find_element_by_xpath('//div[@aria-labelledby="ui-id-{}"]'.format(name+1)).get_attribute('innerHTML')
            cruelty = BeautifulSoup(html, 'lxml')
            df['CRUELTY FREE'][i] = cruelty.text
        elif ltl_ls[name].upper()  == 'DELIVERY & RETURNS':
            html = driver.find_element_by_xpath('//div[@aria-labelledby="ui-id-{}"]'.format(name+1)).get_attribute('innerHTML')
            delivery = BeautifulSoup(html, 'lxml')
            df['DELIVERY & RETURNS'][i] = delivery.text
        elif ltl_ls[name].upper()  == 'VEGAN/GLUTEN':
            html = driver.find_element_by_xpath('//div[@aria-labelledby="ui-id-{}"]'.format(name+1)).get_attribute('innerHTML')
            vegan = BeautifulSoup(html, 'lxml')
            df['VEGAN/GLUTEN'][i] = vegan.text

    df['Category/Sub-category'][i] = cat

    try:
        colours = driver.find_elements_by_tag_name('option')
        colour = ""
        for c in range(1,len(colours)):
            colour = colour + colours[c].text + "\n"
        df['Attributes'][i] = colour
    except Exception as e:
        pass

    try:
        video = driver.find_element_by_xpath('//div[@class="Video-Tutorial"]//embed').get_attribute('src')
        df['Video_url'][i] = video
    except Exception as e:
        pass

    try:
        img_url = driver.find_element_by_xpath('//img[@id="cloudZoomImage"]').get_attribute('src')
        df['Image_url'][i] = img_url
    except Exception as e:
        pass

for site in ls_all:
    driver.get(site)
    time.sleep(5)

    items = driver.find_elements_by_xpath('//div[@class="item-box"]')
    for x in range(len(items)):
        html = items[x].get_attribute('innerHTML')
        soup = BeautifulSoup(html, 'lxml')
        tags = soup.find_all('a')
        sub = tags[1].text
        big_ls.append(['{}/{sub}'.format('makeup', sub),'https://www.janeiredale.co.uk'+tags[1].get('href')+'#/pageSize=12&orderBy=0&pageNumber=1'])


    for z in range(len(big_ls)):
        site = big_ls[z][1]
        driver.get(site)
        time.sleep(5)

        items = driver.find_elements_by_xpath('//div[@class="item-box"]')
        for x in range(len(items)):
            html = items[x].get_attribute('innerHTML')
            soup = BeautifulSoup(html, 'lxml')
            tags = soup.find_all('a')
            ls.append([big_ls[z][0],'https://www.janeiredale.co.uk'+tags[1].get('href')+'#/pageSize=12&orderBy=0&pageNumber=1'])

    for y in range(len(ls)):
        scrap(ls[y][0],ls[y][1],y)



df.to_csv(YOUR-CSV-PATH)
driver.close()
