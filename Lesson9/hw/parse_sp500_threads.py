import asyncio

import requests
import xmltodict
import re
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
from datetime import datetime

root_url = "https://markets.businessinsider.com"
cbrf_cur_url = "https://www.cbr.ru/scripts/XML_daily.asp?date_req="
analysis_data_dict = {}
analysis_parameters_list = ['name','price', 'P/E', 'potential_profit', 'growth']
companies_temp = []
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


def get_companies_details_main_page(page):
    tree = etree.HTML(page)
    r = tree.xpath('//div[@class= "table-responsive"]//tbody/tr/td/a')
    growth = tree.xpath('//div[@class= "table-responsive"]//tbody/tr/td[8]/span[2]')
    for line, value in zip(r, growth):
        companies_temp.append({"url": root_url + line.get("href"), "growth": float(value.text[:-1])})

    
def get_single_company_page_html(company_dict):
    url = company_dict.pop('url')
    page = get_page_html(url)
    return((company_dict, page))


def update_single_company_details(company_dict, page):
    tree = etree.HTML(page)
    company_name_element = tree.xpath('//*[@class = \'price-section__label\']')
    company_dict['name'] = company_name_element[0].text[:-1]
    company_index_element = tree.xpath('//*[@class = \'price-section__category\']/span')
    company_index = company_index_element[0].text[-4:]
    company_dict['code'] = re.findall('[A-Z]{1,5}', company_index)[0]
    company_price_element = tree.xpath('//*[text()=\'Market Cap\']/..')
    try:
        company_price = company_price_element[0].text
        company_price = re.findall("([\\-\\d.]*)\\s([BM])", company_price)
    except:
        return
    if company_price[0][1] == 'B':
        multiplier = 1E9
    else:
        if company_price[0][1] == 'M':
            multiplier = 1E6
    company_price = float(company_price[0][0]) * multiplier * usd_rub
    company_dict['price'] = company_price
    company_52_w_l = extract_float_from_html_field(tree, '//*[text()=\'52 Week Low\']/..')
    company_52_w_h = extract_float_from_html_field(tree, '//*[text()=\'52 Week High\']/..')
    company_dict['potential_profit'] = round(100*(company_52_w_h-company_52_w_l)/company_52_w_l, 2)
    try:
        company_PE = extract_float_from_html_field(tree, '//div[text()=\'P/E Ratio\']/..')
        company_dict['P/E'] = company_PE
    except:
        company_dict['P/E'] = 0
    companies.append(company_dict)


def get_all_companies_data(companies_list, key):
    output = []
    for dict in companies_list:
        output.append(dict.pop(key))
    analysis_data_dict.update({key:output})



def extract_float_from_html_field(tree, xpath):
    element = tree.xpath(xpath)
    float_value = element[0].text
    float_value = re.findall("([\\-\\d]*\\.[\\d]{0,2})", float_value)
    return float(float_value[0])

def print_status_codes(responses: list):
    for r in responses:
        print(r.status_code, end=" ")

def get_10_companies_details():
    pages_count = 10
    urls = []
    for index in range(1, pages_count+1):
        urls.append(root_url + '/index/components/s&p_500?p=' + str(index))
    with ThreadPoolExecutor(max_workers=pages_count) as pool:
        responses = pool.map(get_page_html, urls)
        for response in responses:
            get_companies_details_main_page(response)

def get_companies_details():
    with ThreadPoolExecutor(max_workers=20) as pool:
        data_collection = pool.map(get_single_company_page_html, companies_temp)
        data = list(data_collection)
        for data_entry in data:
            update_single_company_details(*data_entry)

def get_analysis_data():
    for key in analysis_parameters_list:
        get_all_companies_data(companies, key)

def get_top_10(data_dict, values):
    top_10 = [x for _,x in sorted(zip(data_dict[values], data_dict['name']))][:10]
    return top_10



get_10_companies_details()
get_companies_details()
#collected companies_details
print(companies)
get_analysis_data()
#collected top 10 ratings
sorted_by_price = get_top_10(analysis_data_dict, 'price')
sorted_by_potential_profit = get_top_10(analysis_data_dict, 'potential_profit')
sorted_by_p_e = get_top_10(analysis_data_dict, 'P/E')
sorted_by_growth = get_top_10(analysis_data_dict, 'growth')
