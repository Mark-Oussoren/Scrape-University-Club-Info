import bs4
import openpyxl
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep, time
import re
import requests
from pathlib import Path
import argparse

def retrieve_clubs(url, chrome, user_agent):
    driver = webdriver.Chrome(executable_path=chrome)
    driver.get(url)
    sleep(3)
    resp = requests.get(url, headers={"user-agent": user_agent})
    soup = bs4.BeautifulSoup(resp.content, 'html.parser')
    clubs_found = []
    soup = bs4.BeautifulSoup(driver.page_source, 'lxml')

    load_clubs = driver.find_elements_by_class_name('outlinedButton')[2]
    club_search = []
    num_clubs = 0
    while True:
            try:
                load_clubs.click()
                num_clubs += 10
                sleep(.5)

            except:
                break

    sleep(2)
    for i in range(0, num_clubs - 2):
        try:
            club = driver.execute_script('''
                            return Array.from(document.getElementsByTagName('img'))''')[i + 1]
            sleep(.2)
            club.click()
            sleep(.5)

            try:
                club_name = driver.execute_script('''
                                        return document.querySelector('div[role="main"]').getElementsByTagName('h1')[0].innerText''')

            except:
                club_name = 'NA'

            try:
                e = driver.find_element_by_tag_name('strong')
                club_info = e.find_element_by_xpath('.//ancestor::*').text
                contact_info = re.search(r'[\w\.-]+@[\w\.-]+', club_info).group(0)

            except:
                contact_info = []

            club_profile = {'Club Name': club_name, 'Contact Info': contact_info}
            clubs_found.append(club_profile)
            sleep(.2)
            driver.back()
            sleep(.2)
            print(club_profile)

        except:
            print('Club could not be reached')

    cleaned_clubs = []
    for club in clubs_found:
        if club['Contact Info'] == []:
            pass

        else:
            cleaned_clubs.append(club)

    print(cleaned_clubs)
    club_df = pd.DataFrame(cleaned_clubs)
    club_df.to_excel("Clubs & Contact.xlsx")
    return cleaned_clubs

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--club_site", help="URL of Club - Filter at least one", nargs='?', action='store',
                        default='https://beinvolved.indiana.edu/organizations?categories=6872', type=str)
    parser.add_argument("--chrome", help="Path to Chromedriver 86", nargs='?', action='store', type=str)
    parser.add_argument("--agent", help="User Agent", nargs='?', action='store', type=str)

    args = parser.parse_args()
    url = args.club_size
    chrome = args.chrome
    user_agent = args.agent
    start_time = time()
    clubs = retrieve_clubs(url, chrome, user_agent)
    timed = time() - start_time
    print(f'This took {timed} seconds to scrape club data')

