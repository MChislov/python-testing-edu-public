import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
from datetime import datetime

root_url = "https://markets.businessinsider.com"
cbrf_cur_url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="
companies = []

def get_page_html(url):
    html_text = requests.get(url).text
    return html_text

def get_usr_rub():
    curdate = datetime.today().strftime('%d/%m/%Y')
    data = get_page_html(cbrf_cur_url + curdate)
    print(data)
    tree = etree.ElementTree.parse(data)
    for child in tree.getroot():
        print(child.tag)


    print(curdate)

def get_companies_details_main_page(index):
    text = get_page_html(root_url + '/index/components/s&p_500?p=' + str(index))
    tree = etree.HTML(text)
    r = tree.xpath('//div[@class= "table-responsive"]//tbody/tr/td/a')
    year = tree.xpath('//div[@class= "table-responsive"]//tbody/tr/td[8]/span[2]')
    for line, values in zip(r, year):
        companies.append({line.text: [ {"url": root_url + line.get("href")}, {"year": values.text}]})

#get_companies_details_main_page(1)
#print(companies)
get_usr_rub()


