import sys
import traceback
import urllib

# import aggregate as aggregate
from base64 import b64encode
from multiprocessing.dummy import Process

# import PROXY as PROXY
import self as self
import urllib3
import re
import os
# from ml.models import *
from bs4     import BeautifulSoup as bs, BeautifulSoup
import requests
import time
import datetime
import multiprocessing

from fake_useragent import UserAgent
from proxy_requests import ProxyRequests
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities, Proxy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import ProxyType

CHROMEDRIVER_PATH = "./driver/chromedriver"
import csv
import json
from json import loads
from multiprocessing.pool import ThreadPool
import urllib3
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'SCripts.settings'
django.setup()
from Facebook_Pages.models import FacebookDatapages,Facebook_Category


# def from_browser():
#     from pyvirtualdisplay import Display
#     display = Display(visible=0, size=(1024, 768))
#     display.start()
#     # # vdisplay = xvfbwrapper.Xvfb()
#     # vdisplay.start()
#
#     # launch stuff inside virtual display here
#
#     # vdisplay.stop()
#     chromeoptions = webdriver.ChromeOptions()
#     chromeoptions.add_argument('--disable-notifications')
#     chromeoptions.add_argument('--disable-dev-shm-usage')
#     chromeoptions.add_argument('--shm-size=2g')
#     chromeoptions.add_argument('--no-sandbox')
#     # chromeoptions.add_argument('--headless')
#     chromeoptions.add_argument('--ignore-certificate-errors')
#     browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chromeoptions)
#     return browser
def from_browser():
    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1024, 768))
    display.start()
    fp = webdriver.FirefoxProfile()
    browser = webdriver.Firefox(executable_path='driver/geckodriver',firefox_profile=fp)

    return browser
def find_numbers(str):
    data = re.findall('\d+', str)
    total_countries=len(data)
    total = 0
    for ele in range(0, len(data)):
        total = total + int(data[ele])

    return total,total_countries

browser=from_browser()
browser.get("https://ident.me/")
soup=BeautifulSoup(browser.page_source,'lxml').text
print(soup)
