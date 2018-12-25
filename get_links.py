from bs4 import BeautifulSoup
import requests
from selenium.webdriver.firefox.options import Options
from selenium import webdriver

#get all links with site

def navigate(jun):
    obj = browser.get(jun)
    soup=BeautifulSoup(browser.page_source)
    link = soup.find('div', class_='js-grid-container').find_all('div', class_='description_listing_line pos_rel fs_14 lh_20')
    for i in link:
        l = i.find('a').get('href')
        with open('link_build.txt', 'a') as file:
            file.write('\nwww.novostroy-m.ru'+l)

def main():
    global browser
    browser = webdriver.Firefox()
    global links
    links = []
    urls = []
    for i in range(1,64):
        u = 'https://www.novostroy-m.ru/baza?page='+str(i)+'&per-page=32'
        urls.append(u)
    for jun in urls:
        navigate(jun)
    print('off')
    

if __name__ == '__main__':
    main()
