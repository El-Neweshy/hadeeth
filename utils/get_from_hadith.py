# https://hadith.islam-db.com/single-book/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A/105787/1

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def open_link(link, bab, page):
    final_link = link + str(bab) + '/' + str(page)
    print(link)
    driver.get(final_link)

def get_inf(link):
    return


if __name__ == "__main__":
    global driver
    driver = webdriver.Chrome()

    page = 1
    bab = 1
    while True:
        open_link('https://hadith.islam-db.com/single-book/146/%D8%B5%D8%AD%D9%8A%D8%AD-%D8%A7%D9%84%D8%A8%D8%AE%D8%A7%D8%B1%D9%8A/', bab ,page)
        time.sleep(2)
        page +=1