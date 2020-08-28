# 3869878
# Starting_id=2028396
#https://instagram.pixelunion.net/
import sys
import traceback
import urllib

# import aggregate as aggregate
from multiprocessing.dummy import Process

import urllib3
import re
import os
# from ml.models import *
from bs4     import BeautifulSoup as bs, BeautifulSoup
import requests
import time
import datetime
import multiprocessing
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

# def from_browser():
#     from pyvirtualdisplay import Display
#     display = Display(visible=0, size=(1024, 768))
#     display.start()
#     # vdisplay = xvfbwrapper.Xvfb()
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
    browser = webdriver.Firefox(executable_path='driver/geckodriverfraz',firefox_profile=fp)

    return browser





# data=requests.get('https://www.facebook.com/pages/category/')
url="https://www.facebook.com/pages/category/internet-marketing-service/?page="
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
# path="facebookpageprofile.csv"
def login():
    browser=from_browser()
    browser.get("https://www.facebook.com/")
    username = browser.find_element_by_id("email")
    time.sleep(5)
    password = browser.find_element_by_id("pass")
    time.sleep(3)
    submit = browser.find_element_by_id("loginbutton")
    time.sleep(2)
    username.send_keys("gradyhenderson13@outlook.com")
    password.send_keys("grady13")
    # Step 4) Click Login
    submit.click()
    time.sleep(2)
    return browser
path="facebookpageprofile.csv"

def main():#(s,n):
    browser=login()
    time.sleep(5)
    print("login")
    # for data in csvreader(path)[s:n]:
    #     split=(str(data).split("category/")[1])[:-1]
    #     category=split.replace("-"," ")
    #     # print(category)
    category="ecommerce-website"
    page=1
    while True:
        try:
            if browser.title=="Page not found | Facebook":
                break
            else:
                browser.get("https://ident.me/")
                soup34 = BeautifulSoup(browser.page_source, 'lxml').text
                print(soup34)
                # browser.get(data+"?page="+str(page))
                browser.get("https://www.facebook.com/pages/category/ecommerce-website/")
                print(browser.title)
                soup = BeautifulSoup(browser.page_source, 'html.parser')
                for maindiv in soup.find_all('div', {'class': '_4-u2 _6x0a _4-u8'}):
                    print(maindiv)
                    like_div=maindiv.find('div',{'class':'_6x0f rfloat _ohf'})
                    next_div=like_div.find_next('div')
                    print(next_div.text)

                    try:
                        imgdiv=maindiv.find('div',{'class':'_4bl7 _6x0b'})
                        imglink=imgdiv.find('a')
                        link=imglink['href']
                        print("Page Link=>  "+str(link))
                    except:
                        link=" "
                    try:
                        image=imgdiv.find('img')
                        imagelink=image['src']
                        # print("Image => "+str(imagelink))
                    except:
                        imagelink=" "
                    try:
                        nameanchor=maindiv.find('a',{'class':'_6x0d'})
                        name=nameanchor.text
                        # print("Title => "+str(name))
                    except:
                        name=""
                    try:
                        des=maindiv.find('div',{'class':'_ajw'})
                        desriction=des.text
                        # print("Description =>   "+str(desriction))
                    except:
                        desriction=""
                    try:
                        alldes=maindiv.find('div',{'class':'_4bl9'})
                        alldescription=alldes.text
                        # print("All Description =>   "+str(alldescription))
                    except:
                        alldescription=""

                    try:
                        query_obj = Facebook_Category.objects.filter(name=category)
                        # print(query_obj.exists())
                        if query_obj.exists() == True:
                            query_obj = query_obj[0]
                            # print(query_obj)
                            print('category already exists')
                        else:
                            query_obj = Facebook_Category(name=category)
                            # print(query_obj)
                            query_obj.save()
                            print('category save')
                        facebook_obj = FacebookDatapages.objects.filter(fb_page_link=link).first()
                        if facebook_obj == None:
                            print("new object")
                            getid = query_obj.id
                            facebooksave = FacebookDatapages(
                                category=Facebook_Category(str(getid)),
                                title=str(name),
                                all_Description=str(alldescription),
                                fb_page_link=str(link),
                                # image_url=str(imagelink),
                                Description=str(desriction)

                            )
                            facebooksave.save()
                            print("save")
                    except Exception as e:
                        print(e.__str__())
                        traceback.print_exc()

                    print("//////////////////////////////////*****************************///////////////////////")
        except:
            pass
        page=page+1











if __name__ == '__main__':
    main()

    # import multiprocessing
    # from multiprocessing import process
    # starttime = time.time()
    # processes = []
    # start = 0
    # end = 380
    # for i in range(0, 3):
    #     p = Process(target=main, args=(start, end,))
    #     processes.append(p)
    #     start = end
    #     end = end + 380
    #     p.start()
    #     # time.sleep(2)
    # for process in processes:
    #     process.join()
    #     time.sleep(2)







