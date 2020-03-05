# https://hadith.islam-db.com/narrators/5913/%D8%B9%D9%85%D8%B1-%D8%A8%D9%86-%D8%A7%D9%84%D8%AE%D8%B7%D8%A7%D8%A8-%D8%A8%D9%86-%D9%86%D9%81%D9%8A%D9%84-%D8%A8%D9%86-%D8%B9%D8%A8%D8%AF-%D8%A7...
# https://hadith.islam-db.com/narrators/{}/%D8%B9%D9%85%D8%B1-%D8%A8%D9%86-%D8%A7%D9%84%D8%AE%D8%B7%D8%A7%D8%A8-%D8%A8%D9%86-%D9%86%D9%81%D9%8A%D9%84-%D8%A8%D9%86-%D8%B9%D8%A8%D8%AF-%D8%A7...
# -*- coding: utf-8 -*-

import pandas as pd
from selenium import webdriver
import pprint
import numpy as np


def open_link(page):
    '''
    Open a link and create a global driver given the hadeeth number and hadeeth bab
    '''
    final_link = 'https://hadith.islam-db.com/narrators/{}/%D8%B9%D9%85%D8%B1-%D8%A8%D9%86-%D8%A7%D9%84%D8%AE%D8%B7%D8%A7%D8%A8-%D8%A8%D9%86-%D9%86%D9%81%D9%8A%D9%84-%D8%A8%D9%86-%D8%B9%D8%A8%D8%AF-%D8%A7...' .format(page)
    driver.get(final_link)
    return final_link

def create_csv(file_name):
    columns = [
        "rawy-name",
        "shohra",
        "nasab",
        "rotbah",
        "lived-in",
        "rawy-number-in-webosite",
        "tlameez",
        "Asateza",
        "garh",
        "source-web"
    ]

    df = pd.DataFrame(columns=columns)
    df.index = np.arange(1, len(df) + 1)
    df.to_csv('{}.csv'.format(file_name))
    return df


def get_info(url, df):

    rawy_name = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/h5[1]/span').text
    shohra = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/h5[2]/span').text
    nasab = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/h5[3]/span').text
    rotbah = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/h5[4]/span').text
    lived_in = driver.find_element_by_xpath('//*[@id="collapseOne"]/div/h5[5]/span').text

    tlameez_tag = driver.find_element_by_xpath('//*[@id="collapseTwo"]/div/table/tbody')
    tlameez_trs = tlameez_tag.find_elements_by_tag_name('tr')
    for telmeez_trs in tlameez_trs:
        telmeez_tr_tds = telmeez_trs.find_elements_by_tag_name('td')
        tlameez = []
        for telmeez_tr_td in telmeez_tr_tds:
            telmeez_tr_td_name = telmeez_tr_td[0].text
            telmeez_tr_td_shohra = telmeez_tr_td[1].text
            telmeez_tr_td_rotbah = telmeez_tr_td[2].text
            telmeez_details = "{}, {}, {}".format(telmeez_tr_td_name, telmeez_tr_td_shohra, telmeez_tr_td_rotbah)
            tlameez.append(telmeez_details)

    hadeeth_details = {
        "rawy-name": rawy_name,
        "shohra": shohra,
        "nasab": nasab,
        "rotbah": rotbah,
        "lived-in": lived_in,
        "tlameez": tlameez,
        "Asateza": Asateza,
        "garh": garh,
        "source-web": "https://dorar.net/"
    }

    # Append to csv
    df = df.append(hadeeth_details, ignore_index=True)
    # pprint.pprint(hadeeth_details)
    return hadeeth_details, df


if __name__ == "__main__":
    # Initialize driver
    global driver
    global file_name
    global df
    driver = webdriver.Chrome()

    # Create CSV
    file_name = 'Rowah'
    df = create_csv(file_name)

    # Scrap content
    page = 1
    while page < 3: # Working till 14005
        final_link = open_link(
            'https://hadith.islam-db.com/single-book/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A/1/',
            page)
        df = get_info(driver.current_url, df)[1]
        print('No.:', page, "link", final_link)
        page += 1

    # Finish
    df.to_csv("{}.csv".format(file_name))
    print('Scrap is done check:', "{}.csv".format(file_name))