import traceback
import urllib
import warnings
from pathlib import Path
# import wget as wget
from selenium import webdriver
from bs4 import BeautifulSoup, element
import time
import re
import requests
import urllib3
from urllib.parse import urljoin

from datetime import datetime
from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond

# import mysql.connector
from multiprocessing.pool import ThreadPool
from datetime import date , datetime
# from Amazon.absolute_amazon import *
warnings.filterwarnings("ignore")

def runChromeOverServer():
    while True:
        try:
            # proo = SocksProxies.objects.order_by('count')[0]
            # proxies = proo.proxy
            # proo.count += 1
            # proo.save()
            sockproxy = '172.254.124.231:3128'
            # sockproxy = '104.148.76.149:3128'
            # sockproxy = '104.148.76.152:3128'
            # from pyvirtualdisplay import Display
            # display = Display(visible=0, size=(1024, 768))
            # display.start()
            display = ''
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_experimental_option("excludeSwitches",
                                            ["ignore-certificate-errors", "safebrowsing-disable-download-protection",
                                             "safebrowsing-disable-auto-update",
                                             "disable-client-side-phishing-detection"])
            # options.add_argument('--proxy-server=%s' % sockproxy)
            options.add_argument('--disable-notifications')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--shm-size=2g')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-extensions')
            options.add_argument('--profile-directory=Default')
            options.add_argument("--incognito")
            options.add_argument("--disable-plugins-discovery")
            options.add_argument("--start-maximized")
            options.add_argument("browser.cache.disk.enable")
            options.add_argument("browser.cache.memory.enable")
            options.add_argument("browser.cache.offline.enable")
            options.add_argument("network.http.use-cache");
            while True:
                try:
                    driver = webdriver.Chrome(executable_path=r'driver/chromedriver')
                except:
                    driver = webdriver.Chrome(executable_path=r'driver/chromedriver',
                        chrome_options=options)
                break
            # driver.get("https://www.google.com")
            # time.sleep(10)
            return driver,display

        except Exception as e:
            print('driver while exception')
            exceptionMessage(e)
            pass

def exceptionMessage(e):
    print(traceback.format_exc())
    print('Error on line {}'.format(sys.exc_info()[-1].tb_lineno), type(e).__name__, e)

def youtube_ads():
    driver ,  display = runChromeOverServer()
    driver.get("https://www.youtube.com/watch?v=7rAiZR_zasg")
    time.sleep(2)
    try:
        sCPN_ID = driver.find_element_by_css_selector(".html5-video-info-panel-content").find_element_by_tag_name("div").find_element_by_tag_name("span")
        print(sCPN_ID)
        Ads_Text = driver.find_element_by_css_selector(".ytp-title-text").text.strip()
        print(Ads_Text)

    except:
        print("On startup Vedio Ads not shown")

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".ytp-ad-text-overlay")))
        Ads_panel = driver.find_element_by_css_selector(".ytp-ad-text-overlay").find_element_by_css_selector(".ytp-ad-overlay-title").text
        print(Ads_panel)
    except:
        print("Text_Overlay Ads not shown")


def facebook_ads():
    driver , display = runChromeOverServer()
    driver.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=1614251518827491&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped")
    time.sleep(5)
    try:
        profile_image = driver.find_element_by_css_selector("._8whz").find_element_by_tag_name("img").get_attribute("src")
        profile_Name = driver.find_element_by_css_selector("._8wh_").text
        profile_user_name = driver.find_element_by_css_selector("._8whz").find_element_by_css_selector("._8wi0").text
        follower = driver.find_element_by_css_selector("._8whz").find_element_by_css_selector("._8wi8").find_element_by_css_selector("._8wi7").text
        print(profile_image)
        print(profile_Name)
        print(profile_user_name)
        print(follower)
    except:
        pass


if __name__ == '__main__':
    # youtube_ads()
    facebook_ads()