import re
import os
import time

import requests
import django
from bs4 import BeautifulSoup
from selenium import webdriver

os.environ['DJANGO_SETTINGS_MODULE'] = 'SCripts.settings'
django.setup()
from Facebook_Pages.models import FacebookDatapages,Facebook_Category

def Get_PageID(link,getid):
        # while True:
        #     proxies = {
        #         'http': 'socks5://127.0.0.1:9050',
        #         'https': 'socks5://127.0.0.1:9050'
        #     }
        #     from stem import Signal
        #     from stem.control import Controller
        #     from fake_useragent import UserAgent
        #
        #     headers = {'User-Agent': UserAgent().random}
        #     # print(headers)
        #     with Controller.from_port(port=9051) as c:
        #         c.authenticate('12345')
        #         c.signal(Signal.NEWNYM)
        result = requests.get(str(link))#, proxies=proxies, headers=headers)
        try:
            result = result.text
            profile_id = re.search(r"page_id=[0-9]+", result)
            profile_id = re.search(r"[0-9]+", profile_id.group()).group()
            # print(profile_id)
            if profile_id!="None":

                FacebookDatapages.objects.filter(pk=getid).update(page_id=profile_id)
                print("save")
                # return profile_id
                # break

                # pass
            else:
                pass

        except:
            pass

# for data in FacebookDatapages.objects.values('fb_page_link'):
#     link=data['fb_page_link']
#     print(Get_PageID(link))


def selenium_pageid(name,get_id):
    CHROMEDRIVER_PATH = "driver/chromedriver"

    from pyvirtualdisplay import Display
    display = Display(visible=0, size=(1024, 768))
    display.start()
    # # vdisplay = xvfbwrapper.Xvfb()
    # vdisplay.start()

    # launch stuff inside virtual display here

    # vdisplay.stop()
    chromeoptions = webdriver.ChromeOptions()
    chromeoptions.add_argument('--disable-notifications')
    chromeoptions.add_argument('--disable-dev-shm-usage')
    chromeoptions.add_argument('--shm-size=2g')
    chromeoptions.add_argument('--no-sandbox')
    chromeoptions.add_argument('--headless')
    chromeoptions.add_argument('--ignore-certificate-errors')
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chromeoptions)

    # browser=from_browser()
    while True:
        try:
            browser.get("https://lookup-id.com/#")
            browser.find_element_by_xpath("/html/body/div[4]/form/header/div/div[1]/div/input[1]").send_keys(str(name))
            browser.find_element_by_xpath("/html/body/div[4]/form/header/div/div[1]/div/input[2]").click()
            time.sleep(5)
            test=browser.find_element_by_xpath("/html/body/div[4]/form/header/div/div[3]/div/p[2]/span[1]").text
            FacebookDatapages.objects.filter(pk=get_id).update(page_id=test)
            print("save")
            break
        except:
            pass
if __name__ == '__main__':
    # def suggest_cat(s, n):
    #     # list = []
    #     count = 0
    #     a = FacebookDatapages.objects.all().values('fb_page_link','id').filter(page_id__isnull=True).order_by('-id')[s:n]
    #     for amazon_main_cat in a:
    #         get_id=amazon_main_cat['id']
    #         name = amazon_main_cat['fb_page_link']
    #         # list.append(name)
    #         selenium_pageid(name,get_id)
    # #
    # #
    # from multiprocessing import Process
    #
    # starttime = time.time()
    # processes = []
    # start = 0
    # end = 100
    # for i in range(0, 100):
    #     p = Process(target=suggest_cat, args=(start, end,))
    #     processes.append(p)
    #     start = end
    #     end = end + 100
    #     p.start()
    #     time.sleep(2)
    # for process in processes:
    #     process.join()
    #     time.sleep(2)

    #
    # for data in FacebookDatapages.objects.values('fb_page_link').order_by("id")[1:25]:
    #     print(str(data['fb_page_link']))
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
        browser = webdriver.Chrome(executable_path="driver/chromedriver", chrome_options=chromeoptions)
        return browser

    def test(s,n):
        from selenium.webdriver.common.keys import Keys
        browser=from_browser()
        browser.get("https://megritools.com/bulk-facebook-id-finder")

        for data in FacebookDatapages.objects.values('fb_page_link').order_by("id")[s:n]:
            # print(str(data['fb_page_link']))
            browser.find_element_by_css_selector("#linksBox").send_keys(str(data['fb_page_link'])+Keys.ENTER)
        browser.find_element_by_css_selector("#checkButton").click()
        time.sleep(30)
        soup=BeautifulSoup(browser.page_source, 'lxml')

        for table in soup.find_all('table',{'id':'resTable'}):
            num=0
            for tr in table.find_all('tr')[1:]:
                # td = tr.find_all('td')
                link=tr.find('td',{'id':'link-'+str(num)})
                print(link.text)
                page_number=tr.find('td',{'id':'status-'+str(num)}).text
                print(page_number)
                num=num+1


    # test(1,25)

    def get_link(s,n):
        for data in FacebookDatapages.objects.values('fb_page_link').order_by("id")[s:n]:
            for link in data:

            # get_id=amazon_main_cat['id']
            #         name = amazon_main_cat['fb_page_link']
            #         # list.append(name)
            #         selenium_pageid(name,get_id)
    # from multiprocessing import Process
    #
    # starttime = time.time()
    # processes = []
    # start = 0
    # end = 25
    # for i in range(0, 5):
    #     p = Process(target=test, args=(start, end,))
    #     processes.append(p)
    #     start = end
    #     end = end + 25
    #     p.start()
    #     time.sleep(2)
    # for process in processes:
    #     process.join()
    #     time.sleep(2)