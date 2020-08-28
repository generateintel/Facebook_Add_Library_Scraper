import paramiko
from scp import SCPClient
import os
import requests
dir_path = os.path.dirname(os.path.abspath(__file__))
print(dir_path)
def uploadFunction():
    try:
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect('73.137.12.79', 22, 'Cronjobs!9')
        print("Here1")
        scp = SCPClient(client.get_transport())
        pathofifl=dir_path+'/'+'ZIP'+'/'
        ABC=os.listdir(dir_path+ '/' + 'ZIP')
        print("Here2")
        for filename in ABC:
            print(filename)
            scp.put(files= pathofifl + filename,
                remote_path='/home/linuxadmin/Scripts/')
        client.close()
        scp.close()
    except Exception as e:
        print(e)
uploadFunction()
print("Uploaded")
#=========================================
# import paramiko
# from scp import SCPClient
# import os
# import requests
# dir_path = os.path.dirname(os.path.abspath(__file__))
# print(dir_path)
# def uploadFunction():
#     try:
#         client = paramiko.SSHClient()
#         client.load_system_host_keys()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect('169.45.227.162', 7722, 'root', 'TEHRNTq7')
#         scp = SCPClient(client.get_transport())
#         pathofifl=dir_path+'/'+'ZIP'+'/'
#         ABC=os.listdir(dir_path+ '/' + 'ZIP')
#         for filename in ABC:
#             print(filename)
#             scp.put(files= pathofifl + filename,
#                 remote_path='/root/fraz/gen/SCripts')
#         client.close()
#         scp.close()
#     except Exception as e:
#         print(e)
# uploadFunction()
# print("Uploaded")
#===========================================New Server==================================================
# import paramiko
# from scp import SCPClient
# import os
# import requests
# dir_path = os.path.dirname(os.path.abspath(__file__))
# print(dir_path)
# def uploadFunction():
#     try:
#         client = paramiko.SSHClient()
#         client.load_system_host_keys()
#         client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         client.connect('35.223.77.216', 22, 'root')
#         scp = SCPClient(client.get_transport())
#         pathofifl=dir_path+'/'+'ZIP'+'/'
#         ABC=os.listdir(dir_path+ '/' + 'ZIP')
#         for filename in ABC:
#             print(filename)
#             scp.put(files= pathofifl + filename,
#                 remote_path='/root/influx/')
#         client.close()
#         scp.close()
#     except Exception as e:
#         print(e)
# uploadFunction()
# print("Uploaded")
#===================================
# # #https://instagram.pixelunion.net/
# import sys
# import urllib
# import urllib3
# import re
# import os
# import django
# # # from ml.models import *
# from bs4 import BeautifulSoup as bs, BeautifulSoup
# import requests
# import time
# import datetime
# import multiprocessing
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
#
# CHROMEDRIVER_PATH = "driver/chromedriver"
# import csv
# import json
# from json import loads
# from multiprocessing.pool import ThreadPool
#
# os.environ['DJANGO_SETTINGS_MODULE'] = 'influexp.settings'
# django.setup()
# from ml.models import *
#
# usernamelist = []
# import urllib3
#
# # ==========================
# soup1 = ""
# view = 0
# tag = 0
# geotag = 0
# faves = 0
# group = 0
# likeperpost = 0
# commentperpost = 0
# er = 0.0
# num = 0
# like = 0
# comment = 0
# data = {}
# totalphoto = ""
# profileimage = ""
# profilelink = ""
# Rank = None
# name = ""
# followers = None
# joindate = ""
# # liker=0
# location = ""
# email = ""
# # commentr=0
# weblink = ""
# description = ""
# getid = None
# facebook = ""
# twitter = ""
# instagram = ""
# pinterest = ""
#
#
# # #===========================
# def internet_on():
#     http = urllib3.PoolManager()
#     r = http.request('GET', 'http://httpbin.org/robots.txt')
#     if r.status == 200:
#         return True
#     else:
#         return False
#
#
# def strip(row):
#     data = (str(row).strip("[]")).strip("''")
#     return data
#
#
# test = []
#
#
# def csvreader(path):
#     import csv
#     with open(path, 'r') as csvFile:
#         row = []
#         reader = csv.reader(csvFile)
#         for row in reader:
#             try:
#                 clstrip = strip(row)
#                 test.append(clstrip)
#             except:
#                 pass
#         # print(test)
#
#     csvFile.close()
#     return test
#
#
# domain = "https://www.flickr.com"
#
#
# def pff(data):
#     lidata = (data).split(" ")[0]
#     if 'K' in lidata or 'k' in lidata:
#         # print(value)
#         a1 = lidata[:-1]
#         # print(a1)
#         a2 = float(a1) * 1000
#         lidata = a2
#     elif 'M' in lidata or 'm' in lidata:
#         a1 = lidata[:-1]
#         a2 = float(a1) * 1000000
#         lidata = a2
#     return lidata
#
#
# def rank(followers, following, post):
#     rank = int(followers) * .45 + int(following) * .20 + int(post) * .35
#     # print("FIR", rank)
#     rank = int(rank)
#
#     if len(str(rank)) > 5:
#         a = 1
#         r = []
#         sub1 = str(rank)[1:5]
#         sub2 = str(rank)[2:5]
#         aaa = len(str(rank)) - 5
#         # print(aaa)
#         if aaa == 3:
#             r.append(7)
#         elif aaa == 4:
#             r.append(8)
#             aa = str(rank)[-1:5]
#         elif aaa > 4:
#             r.append(9)
#         elif aaa == 2:
#             r.append(6)
#         elif aaa == 1:
#             r.append(5)
#         else:
#             r.append(4)
#
#         if int(r[0]) > int(str(rank)[0]):
#             R = int(r[0]) * 100000 + int(str(rank)[0]) * 10000 + int(sub2)
#             rank = R
#             # print(rank)
#         else:
#             R = int(str(rank)[0]) * 100000 + int(str(rank)[0]) * 10000 + int(sub2)
#             rank = R
#             # print(rank)
#     else:
#         print("no rank")
#     return rank
#
#
# def inserttodatabase(data):
#     print("here")
#     try:
#         GovernmentBidsProfile_objects = flickr_profiles(
#             flickr_categories_keys=flickr_categories(str(data.get('category'))),
#             image_count=data.get('image_count'),
#             image_link=str(data.get('image_link')),
#             profile_linked=str(data.get('profile_linked')),
#             profile_rank=data.get('profile_rank'),
#             profile_name=str(data.get('profile_name')),
#             followers=data.get('followers'),
#             joined_date=str(data.get('joined_date')),
#             hometown=str(data.get('hometown')),
#             website=str(data.get('website')),
#             description=str(data.get('description')),
#             views_total=(data.get('views_total')),
#             tags=(data.get('tags')),
#             geotags=(data.get('geotags')),
#             faves=(data.get('faves')),
#             groups=(data.get('groups')),
#             er=(data.get('er')),
#             likeperpost=(data.get('likeperpost')),
#             commentperpoast=(data.get('commentperpoast')),
#             facebook=str(data.get('facebook')),
#             twitter=str(data.get('twitter')),
#             instagram=str(data.get('instagram')),
#             pinterest=str(data.get('pinterest')),
#             email=str(data.get('email')),
#         )
#         GovernmentBidsProfile_objects.save()
#         print("Done allllllllllllllll")
#
#
#     except Exception as e:
#         print(str(e))
#
#
# def flickerscript(path):
#     global getid
#     # from pyvirtualdisplay import Display
#     # display = Display(visible=0, size=(1024, 768))
#     # display.start()
#     chromeoptions = webdriver.ChromeOptions()
#     chromeoptions.add_argument('--disable-notifications')
#     chromeoptions.add_argument('--disable-dev-shm-usage')
#     chromeoptions.add_argument('--shm-size=2g')
#     chromeoptions.add_argument('--no-sandbox')
#     # chromeoptions.add_argument('--headless')
#     browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chromeoptions)
#     while True:
#         try:
#             if internet_on() == False:
#                 time.sleep(5)
#                 pass
#             else:
#                 print("Out")
#                 break
#         except:
#             pass
#     for cat in csvreader(path):
#         try:
#             catsp = (str(cat).split(",")[1]).split("'")[1]
#             # catsp=cat
#             print(catsp)
#             query_obj = flickr_categories.objects.filter(flickr_categories=catsp)
#             # print(query_obj.exists())
#             if query_obj.exists() == True:
#                 # getid=flickr_categories.objects.get(flickr_categories=catsp)
#                 # print(getid.id)
#                 query_obj = query_obj[0]
#                 # getid=query_obj.id
#                 print('category already exists')
#             else:
#                 query_obj = flickr_categories(flickr_categories=catsp)
#                 # print(query_obj)
#                 query_obj.save()
#                 print('category save')
#                 # check = flickr_categories.objects.latest('id')
#                 # getid = str(check.id)
#             # browser.get("https://www.flickr.com/search/people/?username=food")#"https://www.flickr.com/search/people/?username="+cat)
#             browser.get("https://www.flickr.com/search/people/?username=" + catsp)
#             time.sleep(2)
#             elem = browser.find_element_by_tag_name("body")
#             no_of_pagedowns = 40
#             while no_of_pagedowns:
#                 # while internet() == False:
#                 #     time.sleep(5)
#                 elem.send_keys(Keys.PAGE_DOWN)
#                 time.sleep(0.2)
#                 no_of_pagedowns -= 1
#             soup = BeautifulSoup(browser.page_source, "html.parser")
#             time.sleep(2)
#             for div in soup.find_all('div', {'class': 'result-card linked reboot-restyle'}):
#                 link = div.find('a', {'class': 'click-anywhere'})
#                 profilelink = domain + link['href']
#                 number = 0
#                 Bidlink = str(profilelink)
#                 flickrpro_obj = flickr_profiles.objects.filter(profile_linked=Bidlink).first()
#                 # objs = flickr_profiles.objects.raw('select * from ml_flickr_profiles WHERE profile_linked = %s',[Bidlink])
#                 if flickrpro_obj == None:
#                     # for data in objs:
#                     #     number = number + 1
#                     # # print(number)
#                     # if number > 0:
#                     #     print(number)
#                     #     print("Not insert//////////////")
#                     # else:
#                     print("new object")
#                     getid = query_obj.id
#                     # print(getid)
#                     infludetails(profilelink, browser, getid)
#         except Exception as ex:
#             # pass
#             template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#             message = template.format(type(ex).__name__, ex.args)
#             print(message)
#         print("///////////////////////////////////////////////////////////")
#
#
# proimagedomain = "https://farm9."
#
#
# def removequt(followers):
#     if "," in followers:
#         followers = followers.replace(",", "")
#         # print(followers)
#     else:
#         followers = followers
#     return followers
#
#
# def infludetails():#profilelink, browser, getid):
#     global data
#     global view
#     global tag
#     global geotag
#     global faves
#     global group
#     global likeperpost
#     global commentperpost
#     global er
#     # global commentr
#     global num
#     global like
#     global comment
#     global totalphoto
#     global profileimage
#     global Rank
#     global name
#     global followers
#     global joindate
#     global location
#     global weblink
#     global description
#     global soup1
#     # global liker
#     totalphoto = 0
#     followers = 0
#     # browser.delete_all_cookies()
#     profilelink="https://www.flickr.com/people/123721974@N04/"
#     browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)#, chrome_options=chromeoptions)
#     browser.get(profilelink)
#     soup = BeautifulSoup(browser.page_source, "html.parser")
#     div = soup.find('div', {'class': 'coverphoto-content fluid-centered'})
#     try:
#         proimageget = div.find('div', {'class': 'avatar no-menu person large no-edit'})
#         profileimage = proimagedomain + (str(proimageget['style']).split("//live.")[1]).split(");")[0]
#         # print(profileimage)
#     except:
#         pass
#     try:
#         h1 = div.find('h1', {'class': 'truncate'})
#         name = h1.text
#         # print(name)
#     except:
#         pass
#     try:
#         subtitlle = div.find('p', {'class': 'subtitle no-shrink truncate'})
#         title = subtitlle.text
#         # print(title)
#     except:
#         pass
#     try:
#         follow = div.find('p', {'class': 'followers truncate no-shrink'})
#         followerssplit = str(follow.text).split("•")
#         followers = (followerssplit[0]).split(" ")[0]
#         followers = pff(followers)
#         followers = removequt(followers)
#         # print(followers)
#     except:
#         pass
#     try:
#         following = (followerssplit[1]).split(" ")[0]
#         following = pff(following)
#         following = removequt(following)
#     except:
#         pass
#     try:
#         post = 0
#         Rank = rank(followers, following, post)
#         # print(Rank)
#     except:
#         pass
#     try:
#         photo = div.find('p', {'class': 'metadata-item photo-count'})
#         totalphoto = str(photo.text).split(" ")[0]
#         totalphoto = removequt(totalphoto)
#         # print(totalphoto)
#     except:
#         pass
#     try:
#         loc = div.find('p', {'class': 'metadata-item truncate cp-location loc'})
#         location = loc.text
#         # print(location)
#     except:
#         pass
#     try:
#         join = div.find('p', {'class': 'metadata-item joined'})
#         joindate = join.text
#         # print(joindate)
#     except:
#         pass
#
#     try:
#         browser.find_element_by_xpath("//*[@id='about']/a").click()
#         time.sleep(2)
#         soup1 = BeautifulSoup(browser.page_source, "html.parser")
#         # print(soup1.prettify())
#         maindiv = soup1.find('div', {'class': 'bio-description section'})
#         # print(soup1.prettify())
#         try:
#             contactinformation = otherinfoemartion(maindiv)
#             # print(contactinformation['email'])
#
#         except:
#             pass
#         try:
#             div = maindiv.find('div', {'class': 'description-container'})
#             description = div.text
#             # print(description)
#         except:
#             pass
#         try:
#             mainul = maindiv.find('ul')
#             mainulnext = mainul.find_next('ul')
#             try:
#                 linext = mainulnext.find('li')
#                 webspan = linext.find('span')
#                 weblink = str(webspan.text)
#                 if weblink == 'Website':
#                     weblinkspan = webspan.find_next('span')
#                     weblink = weblinkspan.text
#                     # print(weblink)
#             except:
#                 pass
#         except:
#             pass
#         try:
#             # time.sleep(3)
#             footerli = maindiv.find('div', {'class': 'general-stats'})
#             viewli = footerli.find('li')
#             # print(viewli.text)
#             view = float(pff(viewli.text))
#             # print(view)
#         except:
#             pass
#         try:
#             tagli = viewli.find_next('li')
#             tag = float(pff(tagli.text))
#             # print(tag)
#         except:
#             pass
#         try:
#             geoli = tagli.find_next('li')
#             geotag = float(pff(geoli.text))
#             # print(geotag)
#         except:
#             pass
#         try:
#             favli = geoli.find_next('li')
#             faves = float(pff(favli.text))
#             # print(faves)
#         except:
#             pass
#         try:
#             grpli = favli.find_next('li')
#             group = float(pff(grpli.text))
#             # print(group)
#         except:
#             pass
#         try:
#             for popular in soup1.find_all('div',{'class':'popular-container'}):
#                 for a in popular.find_all('a', {'class': 'overlay'}):
#                     likecommlink=domain+a['href']
#                     # print(likecommlink)
#                     req=requests.get(likecommlink)
#                     # browser.get(likecommlink)
#                     lik = BeautifulSoup(req.text, "lxml")
#                     try:
#                         fave=lik.find('span',{'class':'fave-count-label'})
#                         liker = str(fave.text)
#                         # print(liker)
#                         like = like + int(liker)
#                         # print(like)
#                     except:
#                         print("Error ")
#                     try:
#                         comm = lik.find('span', {'class': 'comment-count-label'})
#                         commentr = str(comm.text)
#                         comment = comment + int(commentr)
#                     except:
#                         pass
#                     num=num+1
#             print(like)
#             print(comment)
#                     # engagementdiv = post.find('div', {'class': 'engagement'})
#                     # #print("saxs")
#                     #
#                     # try:
#                     #     fave = engagementdiv.find('span', {'class': 'engagement-item fave'})
#                     #
#                     #     liker = int(fave.text)
#                     #     # print(liker)
#                     #     like = like + liker
#                     #
#                     # except:
#                     #     pass
#                     # try:
#                     #     comm = engagementdiv.find('span', {'class': 'engagement-count'})
#                     #     commentr = comm.text
#                     #     if commentr==" ":
#                     #         commentr=0
#                     #     comment = comment + int(commentr)
#                     # except:
#                     #     pass
#
#                     # num = num + 1
#             # print("Comments"+comment)
#             likeperpost, commentperpost = likecomentperpost(like, comment, num)
#             er = engagement_rate(likeperpost, commentperpost, followers)
#         except:
#             print("Error to find Engag")
#         try:
#             data = {
#                 'image_count': totalphoto,
#                 'image_link': profileimage,  # Change
#                 'profile_linked': profilelink,
#                 'profile_rank': Rank,  # change
#                 'profile_name': name,
#                 'followers': followers,  # change
#                 'joined_date': joindate,  # change
#                 'hometown': location,  # change
#                 'website': weblink,
#                 'description': description,
#                 "category": getid,
#                 "views_total": view,
#                 "tags": tag,
#                 "geotags": geotag,
#                 "faves": faves,
#                 "groups": group,
#                 "er": er,
#                 "likeperpost": likeperpost,
#                 "commentperpoast": commentperpost,
#                 "facebook": contactinformation['facebook'],
#                 "twitter": contactinformation['twitter'],
#                 "instagram": contactinformation['instagram'],
#                 "pinterest": contactinformation['pinterest'],
#                 "email": contactinformation['email'],
#             }
#             print(data)
#
#             # inserttodatabase(data)
#             weblink = ""
#             data.clear()
#             # totalphoto=None,
#             # profileimage=None,  # Change
#             # profilelink=None,
#             # Rank=None,  # change
#             # name=None,
#             # followers=None,  # change
#             # joindate=None,  # change
#             # location=None,  # change
#             # weblink=="",
#             # description=None,
#             # getid=None,
#             # view=None,
#             # tag=None,
#             # geotag=None,
#             # faves=None,
#             # group=None,
#             # er=None,
#             # likeperpost=None,
#             # commentperpost=None,
#         except:
#             print("Errro in database")
#     except Exception as ex:
#         # pass
#         template = "An exception of type {0} occurred. Arguments:\n{1!r}"
#         message = template.format(type(ex).__name__, ex.args)
#         print(message)
#
#
# # flickerscript()
# path0 = "category/fcat.csv"
# path1 = "Influencers_Categories01.csv"
# path2 = "Influencers_Categories02.csv"
# path3 = "Influencers_Categories03.csv"
# path4 = "Influencers_Categories04.csv"
# path5 = "Influencers_Categories05.csv"
# path6 = "Influencers_Categories06.csv"
# path7 = "Influencers_Categories07.csv"
# path8 = "Influencers_Categories08.csv"
# path9 = "Influencers_Categories09.csv"
# path10 = "Influencers_Categories10.csv"
# path11 = "Influencers_Categories11.csv"
# from grabcont import mainfun
#
#
# def siteinformation(url):
#     twingdic = {}
#     try:
#         twingdic.update(mainfun(url))
#         return twingdic
#     except:
#         return twingdic
#
#
# def otherinfoemartion(content):
#     global email
#     global facebook
#     global twitter
#     global instagram
#     global pinterest
#     import re
#     for li in content.find_all('a'):
#         link = str(li['href'])
#         if (re.findall("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", link)):
#             email = link
#             # print(email)
#         elif (re.findall(
#                 "((?:(?:http|https):\/\/)?(?:www.)?facebook.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?)",
#                 link)):
#             facebook = link
#         elif (re.findall(
#                 "((?:(?:http|https):\/\/)?(?:www.)?twitter.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?)",
#                 link)):
#             twitter = link
#         elif (re.findall(
#                 "((?:(?:http|https):\/\/)?(?:www.)?instagram.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?)",
#                 link)):
#             instagram = link
#         elif (re.findall(
#                 "((?:(?:http|https):\/\/)?(?:www.)?pinterest.com\/(?:(?:\w)*#!\/)?(?:pages\/)?(?:[?\w\-]*\/)?(?:profile.php\?id=(?=\d.*))?([\w\-]*)?)",
#                 link)):
#             pinterest = link
#     aboutdic = {'email': email, 'facebook': facebook, 'twitter': twitter, 'instagram': instagram,
#                 'pinterest': pinterest}
#     # print(aboutdic)
#     email = ""
#     facebook = ""
#     twitter = ""
#     instagram = ""
#     pinterest = ""
#     return aboutdic
#     # aboutdic.clear()
#
#
# def likecomentperpost(like, comment, num):
#     print(num)
#     try:
#         like = int(like / num)
#         # print(like)
#     except:
#         pass
#     try:
#         comment = int(comment / num)
#         # print(comment)
#     except:
#         pass
#     return like, comment
#
#
# def engagement_rate(like, comment, followers):
#     like = float(like)
#     comment = float(comment)
#     followers = float(followers)
#     zer0 = 0
#
#     if followers == zer0:
#         engagement_rate = 0.0
#         return engagement_rate
#     else:
#         likepluscomment = like + comment
#         engagement_rate1 = likepluscomment / followers
#         if engagement_rate1 == zer0:
#             engagement_rate = 0.0
#             return engagement_rate
#         else:
#             engagement_rate2 = engagement_rate1 * 100
#             engagement_rate = float(engagement_rate2)
#             # print(engagement_rate)
#             return engagement_rate
#
#
# import threading
# from threading import Thread
#
# threads = []
# import multiprocessing
# from multiprocessing import Process
#
# if __name__ == '__main__':
#     infludetails()
#     # # for path in p:
#     # #     process = Thread(target=mediumscript(path))
#     # #     process.start()
#     # #     threads.append(process)
#     # # for process in threads:
#     # #     process.join()
#     # # thread1 = multiprocessing.Process(target = mediumscript(path1))
#     # # thread2 = multiprocessing.Process(target=mediumscript(path2))
#     # # thread1.start()
#     # # thread2.start()
#     # p1 = Process(target=flickerscript, args=(path1,))
#     # # p2 = Process(target=flickerscript, args=(path2,))
#     # # p3 = Process(target=flickerscript, args=(path3,))
#     # # p4 = Process(target=flickerscript, args=(path4,))
#     # # p5 = Process(target=flickerscript, args=(path5,))
#     # # p6 = Process(target=flickerscript, args=(path6,))
#     # # p7 = Process(target=flickerscript, args=(path7,))
#     # # p8 = Process(target=flickerscript, args=(path8,))
#     # # p9 = Process(target=flickerscript, args=(path9,))
#     # # p10 = Process(target=flickerscript, args=(path10,))
#     # # p11 = Process(target=flickerscript, args=(path11,))
#     # p1.start()
#     # # p2.start()
#     # # p3.start()
#     # # p4.start()
#     # # p5.start()
#     # # p6.start()
#     # # p7.start()
#     # # p8.start()
#     # # p9.start()
#     # # p10.start()
#     # # p11.start()
#     # p1.join()
#     # time.sleep(1)
#     # # p2.join()
#     # # time.sleep(1)
#     # # p3.join()
#     # # time.sleep(1)
#     # # p4.join()
#     # # time.sleep(1)
#     # # p5.join()
#     # # time.sleep(1)
#     # # p6.join()
#     # # time.sleep(1)
#     # # p7.join()
#     # # time.sleep(1)
#     # # p8.join()
#     # # time.sleep(1)
#     # # p9.join()
#     # # time.sleep(1)
#     # # p10.join()
#     # # time.sleep(1)
#     # # p11.join()
