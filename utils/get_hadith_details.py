# https://hadith.islam-db.com/single-book/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A/105787/1
# https://hadith.islam-db.com/single-book/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A/1/1
# https://hadith.islam-db.com/books/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A

# -*- coding: utf-8 -*-

import pandas as pd
from selenium import webdriver
import pprint
import numpy as np


def open_link(link, page):
    '''
    Open a link and create a global driver given the hadeeth number and hadeeth bab
    '''
    final_link = link + str(page)
    print(link)
    driver.get(final_link)


def create_csv(file_name):
    columns = [
        "source-book",
        "source-web",
        "source-url",
        "hadeeth-number",
        "hadeeth",
        "matn",
        "rowah",
        "rowah-number"
    ]

    df = pd.DataFrame(columns=columns)
    df.index = np.arange(1, len(df) + 1)
    df.to_csv('{}.csv'.format(file_name))
    return df

def get_info(url, df):
    hadeeth_obj = driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[1]/div[2]/div[2]/div[2]/p')
    hadeeth = hadeeth_obj.text

    rowah_obj = hadeeth_obj.find_elements_by_class_name('rawy')
    rowah = []
    [rowah.append(rawy.text) for rawy in rowah_obj]

    matn = hadeeth_obj.find_element_by_class_name('matn').text

    hadeeth_number = driver.find_element_by_xpath('//*[@id="hadithid"]').text

    rowah_number = len(rowah)

    source_book = driver.find_element_by_xpath('/html/body/div/div/div/div/ol/li[2]/a').text

    hadeeth_details = {
        "source-book": source_book,
        "source-web": "https://dorar.net/",
        "source-url": url,
        "hadeeth-number": hadeeth_number,
        "hadeeth": hadeeth,
        "matn": matn,
        "rowah": rowah,
        "rowah-number": rowah_number
    }

    # Append to csv
    df = df.append(hadeeth_details, ignore_index=True)

    # pprint.pprint(hadeeth_details)
    return hadeeth_details, df


if __name__ == "__main__":
    # Initialize driver
    global driver
    global book_file_name
    global df
    driver = webdriver.Chrome()

    # Create CSV

    book_file_name = 'صحيح البخاري'
    df = create_csv(book_file_name)

    # Scrap content
    page = 1
    while page < 7032:
        print('page:', page)
        open_link(
            'https://hadith.islam-db.com/single-book/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A/1/',
            page)
        df = get_info(driver.current_url, df)[1]
        page += 1

    # Finish
    df.to_csv("{}.csv".format(book_file_name))
    print('Scrap is done check:', "{}.csv".format(book_file_name))