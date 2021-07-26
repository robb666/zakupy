#!/bin/python3
import sys
import os
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

os.chdir('/home/robb/Desktop/PROJEKTY/zakupy')
sys.setrecursionlimit(10**6)


def logowanie(payload, headers):
    url_log = 'https://www.e-piotripawel.pl/klient/logowanie'
    with requests.Session() as s:
        s.post(url_log, data=payload, headers=headers)
    return s


def dostawy(s):
    term = s.get('https://www.e-piotripawel.pl/koszyk/terminy')
    return BeautifulSoup(term.text, 'lxml')


def terminy(soup):
    for tag in soup.find_all('td', class_="available"):
        data = str(tag).split()
        if len(data) > 9 and data[1] == 'class="available">' and 'checked="checked"' not in data:
            availability = 'td.available'
            return data, availability
    print('Brak terminów w "P&P"')
    dostawy(s)
    sys.exit()


def wolne_terminy(data):
    day, start, end = data[3][5:], data[4][5:], data[6][:-1]
    return day, start, end


def wolny_termin_klik(s, availability):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")

    dummy_url = '/404error'
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.e-piotripawel.pl' + dummy_url)

    driver.delete_all_cookies()
    for cookie in s.cookies.items():
        driver.add_cookie({"name": cookie[0], "value": cookie[1]})
    time.sleep(.4)
    driver.get('https://www.e-piotripawel.pl/koszyk/terminy')
    subject_pos, subject_neg = 'Wolny termin w "Piotr i Paweł"', 'Błąd Selenium"'
    try:
        driver.find_element_by_css_selector(availability).click()
        return subject_pos
    except:
        return subject_neg


def email(day, start, end, subject):
    msg = MIMEText(f'Bingo! - {day}, {start} - {end}"\nMasz godzinę na zrobienie zakupów.')
    msg['Subject'] = subject
    msg['From'] = 'robert.patryk.grzelak@gmail.com'
    msg['To'] = "robert.patryk.grzelak@gmail.com"
    s = smtplib.SMTP('smtp.mailgun.org', 587)
    s.login('postmaster@sandbox7869ed4c3baf41c28d93ed01199eebc0.mailgun.org',
            'd420511ffa1c2a5f1661508f81d2a1c5-46ac6b00-92cbad3b')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    print('Sprawdź email.')

    with open(os.environ['PWD'] + '/znalazł', 'w') as f:
        f.write('')
    time.sleep(2)


def spr():
    try:
        with open(os.environ['PWD'] + '/znalazł', 'r'):
            print('Znalezione.')
        sys.exit()
    except IOError:
        email(day, start, end, subject)


if __name__ == '__main__':

    payload = {'store_models_StoreLoginForm[username]': 'Robo',
               'store_models_StoreLoginForm[password]':	'pass'}
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0',
               'Connection': 'False'}

    print(f'\n\t{datetime.now().strftime("%H:%M:%S")} - Szukam terminu dostawy...\n')

    s = logowanie(payload, headers)
    soup = dostawy(s)
    data, availability = terminy(soup)
    day, start, end = wolne_terminy(data)
    subject = wolny_termin_klik(s, availability)

    spr()
