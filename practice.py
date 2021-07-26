ddfgimport sys
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import argparse
from dotenv import load_dotenv
import json
import codecs

print(os.environ['PWD'])
















# def logowanie(payload, headers):
#     url_log = 'https://www.e-piotripawel.pl/klient/logowanie'
#     with requests.Session() as s:
#         s.post(url_log, data=payload, headers=headers)
#     return s
#
#
# def dostawy(s):
#     term = s.get('https://www.e-piotripawel.pl/koszyk/terminy')
#     return BeautifulSoup(term.text, 'lxml')
#
#
# def terminy(soup):
#     for tag in soup.find_all('td', class_="available"):
#         data = str(tag).split()
#         if len(data) > 9 and data[1] == 'class="available">':    # and 'checked="checked"' not in data:
#             print(data)
#             availability = 'td.available'
#             return data, availability
#     # logowanie(payload, headers)
#     time.sleep(2)
#     print('Ładuje ponownie...')
#     dostawy(s)
#     terminy(soup)
#
#
#
#
#
#
# payload = {'store_models_StoreLoginForm[username]': 'Robo',
#            'store_models_StoreLoginForm[password]':	'pikolinian'}
# headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:74.0) Gecko/20100101 Firefox/74.0'}
# print(f'\n\t{datetime.now().strftime("%H:%M:%S")} - Szukam terminu dostawy...\n')
#
# s = logowanie(payload, headers)
# soup = dostawy(s)
#
# terminy(soup)











# def terminy(soup):
#
#     if soup == 10:
#         return print(f'Zupa gotowa {soup}')
#         return
#     else:
#         print(f'Szukam dalej... {soup}')
#         soup += 1
#         yield from terminy(soup)
#
#
# soup = 1
#
#
#
# print(list(terminy(soup)))