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


def from_browser():
    # from pyvirtualdisplay import Display
    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    # # vdisplay = xvfbwrapper.Xvfb()
    # vdisplay.start()

    # launch stuff inside virtual display here

    # vdisplay.stop()
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument('--disable-notifications')
    chromeoptions.add_argument('--disable-dev-shm-usage')
    chromeoptions.add_argument('--shm-size=2g')
    chromeoptions.add_argument('--no-sandbox')
    # chromeoptions.add_argument('--headless')
    chromeoptions.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chromeoptions)
    return browser
# browser=from_browser()
# for test in FacebookDatapages.objects.values('page_id').filter(page_id__isnull=False):
#     number=test['page_id']
#     browser.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id="+str(number)+"&sort_data[direction]=desc&sort_data[mode]=relevancy_monthly_grouped")
#     soup = BeautifulSoup(browser.page_source, 'html.parser')
#     count=0
#     for data in soup.find_all('div',{'class':'_99s5'}):
#         count =count+1
#     print(count)
#
import xlrd
path ='proxy'
def strip(row):
    data=(str(row).strip("[]")).strip("''")
    return data
test=[]
def csvreader(path):
    import csv
    with open(path, 'r') as csvFile:
        row = []
        reader = csv.reader(csvFile)
        for row in reader:
            try:
                clstrip=strip(row)
                test.append(clstrip)
            except:
                pass
        # print(test)

    csvFile.close()
    return test





from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

HOST = "209.127.191.180"
PORT = "80"
def my_proxy(port,user_name,password,ip_add):
        # print(user_name)

        # headers = {'User-Agent': UserAgent().random}
        fp = webdriver.FirefoxProfile()
        # fp.add_argument("--headless")
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.socksUsername",str(user_name))
        fp.set_preference("network.proxy.socksPassword", str(password))
        fp.set_preference("network.proxy.https",str(ip_add))
        fp.set_preference("network.proxy.https_port",int(port))
        fp.set_preference("network.proxy.ssl",str(ip_add))
        # fp.set_preference("-headless")
        fp.set_preference("network.proxy.ssl_port",int(port))

        # fp.set_preference("browser.cache.disk.enable", False)
        # fp.set_preference("browser.cache.memory.enable", False)
        # fp.set_preference("browser.cache.offline.enable", False)
        # fp.set_preference("network.http.use-cache", False)
        # # fp.set_preference("general.useragent.override","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")#UserAgent().random)
        fp.update_preferences()




        browser=webdriver.Firefox(executable_path='driver/geckodriver',firefox_profile=fp)
        wait(browser, 5).until(EC.alert_is_present())
        alert = browser.switch_to_alert()
        alert.send_keys(user_name + Keys.TAB + password)
        time.sleep(5)
        alert.accept()
        # browser.get("https://megritools.com/bulk-facebook-id-finder")
        # browser.get("https://stackoverflow.com/questions/33783394/selenium-webdriver-enter-multiline-text-in-form-without-submitting-it")
        browser.get(
            "https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=1071181619712254")
        return webdriver.Firefox(executable_path='driver/geckodriver',firefox_profile=fp)
def find_numbers(str):
    data = re.findall('\d+', str)
    total_countries=len(data)
    total = 0
    for ele in range(0, len(data)):
        total = total + int(data[ele])

    return total,total_countries


def count(page_id,count_request):

    browser.get("https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=US&impression_search_field=has_impressions_lifetime&view_all_page_id=1071181619712254"+str(page_id))
    soup = BeautifulSoup(browser.page_source, 'lxml')
    page_bio=soup.find('div',{'class':'_8wi9 _3qn7 _61-3 _2fyi _3qnf'})
    try:
        page_name=page_bio.find('div',{'class':'_8wh_'}).text
        # print(page_name)
    except:
        page_name=""
    try:
        page_likes=page_bio.find('div',{'style':'display: flex;'}).text
        page_likes=page_likes.split(" ")[0]
        # print(page_likes)
    except:
        page_likes=""
    try:
        page_followers_inner=page_bio.find('div',{'class':'_8wi8'})
        page_followers=page_followers_inner.find('div',{'class':'_8wi7'}).text
        page_followers=page_followers.split(" ")[0]
        # print(page_followers)

    except:
        page_followers=""
    try:
        page_created_date=page_bio.find('span',{'class':'_3-99'}).text
        # print(page_created_date)
    except:
        page_created_date=""
    try:
        manage_page=page_bio.find('span',{'style':'font-family: Arial, sans-serif; font-size: 12px; line-height: 16px; letter-spacing: normal; font-weight: bold; overflow-wrap: normal; text-align: left; color: rgb(96, 103, 112);'}).text
        total_people,countires=find_numbers(manage_page)
        # print(total_people)
        # print(countires)
    except:
        pass
    scrape_following={
        "page_name":page_name,
        "page_likes":page_likes,
        "page_followers":page_followers,
        "page_created_date":page_created_date,
        "total_people":total_people,
        "countires":countires
    }

    print(scrape_following)
    # elem = browser.find_element_by_tag_name("body")
    # no_of_pagedowns = 3
    # while no_of_pagedowns:
    #     elem.send_keys(Keys.PAGE_DOWN)
    #     time.sleep(0.2)
    #     no_of_pagedowns -= 1
    # soup = BeautifulSoup(browser.page_source, 'lxml')
    #
    # count=0
    # for data in soup.find_all('div',{'class':'_99s5'}):
    #     count =count+1
    # return count

def store_to_csv(text):
    f = open('Facebook_Add.csv', 'a')
    f.write(text)
    f.write("\n")# Give your csv text here.
    ## Python will convert \n to os.linesep
    f.close()
def ip_sheet_reader(index):
    try:
        loc = ("ip_list/List.xlsx")
        wb = xlrd.open_workbook(loc)
        sheet = wb.sheet_by_index(0)
        sheet.cell_value(0, 0)
        index = index
        row = sheet.row_values(index)
        port = int(row[1])
        user_name = row[2]
        password = row[3]
        ip_add = row[4]
    except:
        ip_add=""
        port=""
        user_name=""
        password=""
    return port,user_name,password,ip_add

if __name__ == '__main__':
    my_proxy()


    # browser=from_browser()
    # add=count(browser)
    # print(add)
    # count_request=0
    # ip_number=5    # changeable
    # for data in FacebookDatapages.objects.values('page_id','fb_page_link').filter(page_id__isnull=False):
    #     page_link=data['fb_page_link']
    #     page_id=data['page_id']
    #     if count_request==0:
    #         count_request=count_request+1
    #         port,user_name,password,ip_add=ip_sheet_reader(ip_number)
    #         if ip_add=="":
    #             print("Again Start")
    #             ip_number=1#changeable
    #             port, user_name, password, ip_add = ip_sheet_reader(ip_number)
    #         print(ip_add)
    #         browser = my_proxy(port,user_name,password,ip_add)
    #         add = count(page_id, count_request)
    #         page_add = page_link + "    =======>>>>" + str(add)
    #         store_to_csv(str(page_add))
    #     elif count_request>10:
    #         browser.quit()
    #         count_request =0
    #         ip_number = ip_number + 1
    #     else:
    #         count_request = count_request + 1
    #         add=count(page_id,count_request)
    #         page_add=page_link+"    =======>>>>"+str(add)
    #         store_to_csv(str(page_add))
