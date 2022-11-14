import asyncio

import requests
import xmltodict
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
    response = requests.get(cbrf_cur_url + curdate)
    datadict = xmltodict.parse(response.content)
    for item in datadict['ValCurs']['Valute']:
        if item['CharCode'] == 'USD':
            value = item['Value']
            value = float(value.replace(',', '.'))
            return value


usd_rub = get_usr_rub()


async def get_companies_details_main_page(index):
    text = get_page_html(root_url + '/index/components/s&p_500?p=' + str(index))
    tree = etree.HTML(text)
    r = tree.xpath('//div[@class= "table-responsive"]//tbody/tr/td/a')
    year = tree.xpath('//div[@class= "table-responsive"]//tbody/tr/td[8]/span[2]')
    for line, values in zip(r, year):
        companies.append({line.text: {"url": root_url + line.get("href"), "year": values.text}})


async def update_single_company_details(company_dict, url):
    page = get_page_html(url)
    tree = etree.HTML(page)
    company_index_element = tree.xpath('//*[@class = \'price-section__category\']/span')
    company_index = company_index_element[0].text[-3:]
    company_dict['index'] = company_index
    company_price_element = tree.xpath('//*[text()=\'Market Cap\']/..')
    company_price = company_price_element[0].text
    company_price = re.findall("([\\-\\d.]*)\\s([BM])", company_price)
    if company_price[0][1] == 'B':
        multiplier = 1E9
    else:
        if company_price[0][1] == 'M':
            multiplier = 1E6
    company_price = float(company_price[0][0]) * multiplier * usd_rub
    company_dict['price_rub'] = company_price
    company_52_w_l = extract_float_from_html_field(tree, '//*[text()=\'52 Week Low\']/..')
    company_dict['52_w_l'] = company_52_w_l
    company_52_w_h = extract_float_from_html_field(tree, '//*[text()=\'52 Week High\']/..')
    company_dict['52_w_h'] = company_52_w_h
    try:
        company_PE = extract_float_from_html_field(tree, '//div[text()=\'P/E Ratio\']/..')
        company_dict['PE'] = company_PE
    except:
        company_dict['PE'] = 0
    print(company_dict)



def extract_float_from_html_field(tree, xpath):
    element = tree.xpath(xpath)
    float_value = element[0].text
    float_value = re.findall("([\\-\\d]*\\.[\\d]{0,2})", float_value)
    return float(float_value[0])



# get_companies_details_main_page(1)
# print(companies)

async def get_10_companies_details():
    tasks = [asyncio.create_task(get_companies_details_main_page(item)) for item in range(1, 11)]
    await asyncio.gather(*tasks)

async def get_companies_details():
    params = []
    for company in companies:
        company_key = (list(company.keys())[0])
        params.append((company[company_key], company[company_key]['url']))
    print(params)
    tasks = [asyncio.create_task(update_single_company_details(param[0], param[1])) for param in params]
    await asyncio.gather(*tasks)

asyncio.run(get_10_companies_details())
asyncio.run(get_companies_details())

