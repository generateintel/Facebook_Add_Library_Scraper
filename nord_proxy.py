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

CHROMEDRIVER_PATH = "driver/chromedriver"
import csv
import json
from json import loads
from multiprocessing.pool import ThreadPool
import urllib3
import django
os.environ['DJANGO_SETTINGS_MODULE'] = 'SCripts.settings'
django.setup()
from Facebook_Pages.models import FacebookDatapages,Facebook_Category

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions



# def my_proxy(port, user_name, password, ip_add):
#     # print(user_name)
#
#     headers = {'User-Agent': UserAgent().random}
#     fp = webdriver.FirefoxProfile()
#     # fp.add_argument("--headless")
#     fp.set_preference("network.proxy.socksUsername",str(user_name))
#     fp.set_preference("network.proxy.socksPassword", str(password))
#     fp.set_preference("network.proxy.socks.https", str(ip_add))
#     fp.set_preference("network.proxy.https_port", int(port))
#     fp.set_preference("network.proxy.ssl", str(ip_add))
#     # fp.set_preference("-headless")
#     fp.set_preference("network.proxy.ssl_port", int(port))
#     # fp.set_preference("general.useragent.override","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
#     # fp.set_preference('accept: */*')
#     fp.update_preferences()
#
#     browser = webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
#     # browser.get()
#     browser.get("https://ident.me/")
#     wait(browser, 5).until(EC.alert_is_present())
#     alert = browser.switch_to_alert()
#     alert.send_keys(user_name + Keys.TAB + password)
#     time.sleep(5)
#     alert.accept()
#     # while True:
#     # browser.delete_all_cookies()
#     # browser.header_overrides = {
#     #     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     #     'accept-encoding': 'gzip, deflate, br',
#     #     'accept-language': 'en-US,en;q=0.9',
#     #     # 'content-type': 'application/x-www-form-urlencoded',
#     #     # 'origin': 'https://www.facebook.com',
#     #     # 'referer': 'https://www.google.com/',
#     #     'sec-fetch-dest': 'document',
#     #     'sec-fetch-mode': 'navigate',
#     #     'sec-fetch-site': 'none',
#     #     'user-agent':' Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
#     #     'UPGRADE-INSECURE-REQUESTS':1
#     # }
#
#     browser.get(
#         "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=110217597053361&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped")
#     soup=BeautifulSoup(browser.page_source,'lxml')
#     print(soup.prettify())
#     # browser.get("https://www.facebook.com/")
#     # browser.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=110217597053361&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped")
#
#     # return webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
#
#


def my_proxy(port, user_name, password, ip_add):
    # print(user_name)
    # geckodriver_autoinstaller.install()
    headers = {'User-Agent': UserAgent().random}
    fp = webdriver.FirefoxProfile()

    # fp.add_argument("--headless")

    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http", str(ip_add))
    fp.set_preference("network.proxy.http_port", int(port))
    fp.set_preference("network.proxy.ssl", str(ip_add))
    # fp.
    # fp.set_preference("-headless")
    fp.set_preference("network.proxy.ssl_port", int(port))
    fp.set_preference("network.proxy.ftp", str(ip_add))
    fp.set_preference("network.proxy.ftp_port", int(port))
    fp.set_preference("network.proxy.socks", str(ip_add))
    fp.set_preference('network.proxy.noproxy','aSFasfa')
    fp.set_preference("network.proxy.socks_port", int(port))
    fp.set_preference("browser.cache.disk.enable", False)
    fp.set_preference("browser.cache.memory.enable", False)
    fp.set_preference("browser.cache.offline.enable", False)
    fp.set_preference("network.http.use-cache", False)
    fp.set_preference("network.proxy.Username",str(user_name))
    fp.set_preference("network.proxy.Password", str(password))
    fp.set_preference("general.useragent.override",UserAgent().random)
    fp.update_preferences()

    browser = webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
    time.sleep(3)
    wait(browser, 5).until(EC.alert_is_present())
    alert = browser.switch_to.alert.authenticate
    print("fraz//////")
    alert.send_keys(user_name + Keys.TAB + password)
    time.sleep(1)
    alert.accept()
    # browser.get("https://megritools.com/bulk-facebook-id-finder")
    # browser.get("https://stackoverflow.com/questions/33783394/selenium-webdriver-enter-multiline-text-in-form-without-submitting-it")
    browser.delete_all_cookies()
    browser.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=110217597053361&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped")
    # return webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
    time.sleep(5)




# Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0

my_proxy(80,'fbaileyiii@gmail.com','213500DN','us4878.nordvpn.com')



# fp = webdriver.FirefoxProfile()
# fp.set_preference("network.proxy.type", 1)
# fp.set_preference("network.proxy.socksUsername",str(user_name))
# fp.set_preference("network.proxy.socksPassword", str(password))
# fp.set_preference("network.proxy.https", str(ip_add))
# fp.set_preference("network.proxy.https_port", int(port))
# fp.set_preference("network.proxy.ssl", str(ip_add))
# # fp.set_preference("-headless")
# fp.set_preference("network.proxy.ssl_port", int(port))
# fp.update_preferences()
#
# browser = webdriver.Firefox(executable_path='driver/geckodriver', firefox_profile=fp)
# browser.get("https://ident.me/")
# wait(browser, 5).until(EC.alert_is_present())
# alert = browser.switch_to_alert()
# alert.send_keys(user_name + Keys.TAB + password)
# time.sleep(5)
# alert.accept()